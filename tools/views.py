from django.shortcuts import get_object_or_404, render, redirect
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language, activate, gettext_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from .models import Tool, type_tool, CoinBaseProcess
from account.models import Profile
from django.contrib import messages
from .form import ToolForm
import json
import requests
# Create your views here.


def search_tool(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    tools = Tool.objects.filter(tool_name__icontains=q)
    
    context={
        'tools': tools,
        'q':q,
    }
    return render(request, 'tools/search_results.html', context)


def display_tool(request):
    trans = translate(language='ar')
    tools = Tool.objects.all()
    context={'tools':tools}
    return render(request, 'tools/products.html', context)

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = _('hello')
    finally:
        activate(cur_language)
    return text

# def switch_language(request):
#     if request.method == 'POST':
#         language = request.POST.get('language',  'en') # 'en' is the default language (English)
#         if language in ['en', 'tr', 'ru']: # Ensure the language is one of the available languages
#             print(f"Switching language to {language}")
#             request.session['django_language'] = language
    
#     referring_page = request.META.get('HTTP_REFERER', '/') # Get the referring page or use the homepage as a fallback
#     print(f"Redirecting to {referring_page}")
#     return redirect(referring_page)

@staff_member_required
@login_required()
def add_Tool(request):
    type_tools = type_tool.objects.all()
    if request.method == 'POST':
        form = ToolForm(request.POST, request.FILES)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.username = request.user
            tool.save()
            messages.success(request, _('Tool added successfully'))
            # #حدد نوع الأداة
            # tool_type = form.cleaned_data.get('type_of_tool')
            
            # # أعد توجيه المستخدم إلى القالب المناسب بناءً على نوع الأداة
            # if tool_type == 'smtp':
            #     return redirect('smtp_template')
            # elif tool_type == 'sender':
            #     return redirect('sender_template')
            # elif tool_type == 'shell':
            #     return redirect('shell_template')
            return redirect('display_tool')
            
        else:
            print(form.errors)
            messages.error(request, _('try again'))
            return redirect('add_tool')
    else:
        form = ToolForm()
    
    context={
        'form':form,
        'type_tools':type_tools,
    }
    return render(request, 'tools/tool_form.html', context)


def smtp_template(request):
    tools = Tool.objects.filter(type_of_tool__name='smtp')
    context={'tools':tools}
    return render(request, 'tools/temp_tool/smtp_template.html', context)

def sender_template(request):
    tools = Tool.objects.filter(type_of_tool__name='sender')
    context={'tools':tools}
    return render(request, 'tools/temp_tool/sender_template.html', context)

def shell_template(request):
    tools = Tool.objects.filter(type_of_tool__name='shell')
    context={'tools':tools}
    return render(request, 'tools/temp_tool/shell_template.html', context)


def tool_detail(request, slug):
    tool = get_object_or_404(Tool, slug=slug)
    context={'tool':tool}
    return render(request, 'tools/product.html', context)


@login_required(login_url='login_view')
@staff_member_required
def update_Tool(request, pk):
    tool = get_object_or_404(Tool ,id=pk)
    if request.method == 'POST':
        form = ToolForm(request.POST, request.FILES, instance=tool)
        if form.is_valid():
            form.save()
            messages.success(request, _('Tool updated successfully'))
            return redirect('display_tool')
        
        else:
            messages.error(request, _('try again'))
            return redirect('update_tool')
    else:
        
        form = ToolForm(instance=tool)
    context={'form':form}
    return render(request, 'tools/tool_form.html', context)

@staff_member_required
def delete_Tool(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if request.method == 'POST':
        tool.delete()
        messages.success(request, _('Tool deleted successfully'))
        return redirect('display_tool')
    
    context={'tool':tool}
    return  render(request, 'tools/delete-product.html', context)


@require_POST
def Coinbase_Payment(request, *args, **kwargs):
    post_data = request.POST 
    data = dict() #لتخزين البيانات التي سيتم إرسالها، مثل المعلومات حول المنتج والمبلغ 
    
    headers = dict() #لتخزين المعلومات المتعلقة بالاتصال نفسه
    id = post_data['id'] # id of the tool to  be purchased
    
    product_info = Tool.objects.filter(id=id)
    product_name = product_info[0].tool_name
    
    if product_info:
        product_info = product_info[0]
        price = product_info.price
        user = request.user.email
        api_key = 'f0cecb79-a4b2-436f-a131-b215cbe6fd44'
        url = 'https://api.commerce.coinbase.com/charges'
        
        data['meta_data'] = {
            'id': id,
            'customer': user
        }
        data['name'] = f'Buy {product_name} With {price}'
        data['description'] = 'Sellix Shop'
        data['pricing_type'] = 'fixed_price'
        data['local_price'] = {
            'amount': str(price),
            'currency': 'USD'
        }
        data['cancel_url'] = 'https://localhost.com'
        data['redirect_url'] = 'https://localhost.com'
        headers = {
            'content-type': 'application/json',
            'X-CC-Api-Key': api_key,
            'X-CC-Version': '2018-03-22'
        }
        
        response = requests.post(url=url, data=json.dumps(data), headers=headers)
        confirmed_data = json.loads(response.text)
        try:
            payment_url = confirmed_data['data']['hosted_url']
        except KeyError:
            payment_url = None # or set a default value
        
        return HttpResponseRedirect(payment_url)
    else:
        return redirect('payment')

# لماال api الخاص ب coinbase يبعتلك رد بان العمليه نجحت ول اترفضت والبيانات كمان
def coinbase_postback(request):
    if request.method == 'POST':
        values = json.loads(request.body.decode('utf-8'))
        status = False
        support_email = values['event']['data']['support_email']
        code = values['event']['data']['code']
        product_id = values['event']['data']['metadata']['id']
        value = values['event']['data']['pricing']['local']['amount']
        payment_currency = values['event']['data']['pricing']['local']['currency']
        customer = values['event']['data']['metadata']['customer']
        product_name = values['event']['data']['metadata']['product_name']
        
        for i in values['event']['data']['timeline']:
            if i['status'].lower()  == 'completed' or i['status'].lower() == 'overpaid' or i['status'].lower() == 'confirmed' or i['status'].lower() == 'paid':
                status = True

        if status:
            checkCode = CoinBaseProcess.objects.filter(code=code)
            if not checkCode:
                # New Payment Added
                if support_email == 'azizkrayyem7@gmail.com':
                    # Check about the product
                    # Check product type
                    product_info = Tool.objects.filter(id=int(product_id)).first()
                    if product_info:
                        # check if the product price is correct
                        # use Float To avoid number fraction loss
                        
                        if float(product_info.amount) == float(value) and payment_currency == 'USD':
                            # payment is correct, add the payment
                            CoinBaseProcess.objects.create(
                                code=code,
                                email=customer,
                                amount=value,
                                product_name=product_name,
                                product_id=product_id
                            )
                            # after customer purchase order send notification with tool data 
                            try:
                                user = User.objects.get(email=customer)
                                user_profile = Profile.objects.get(user=user)
                                user_profile.purchased_tools.add(product_info)
                                
                            except User.DoesNotExist:
                                error = _("User does not exist")
                            except user_profile.DoesNotExist:
                                error = _("User profile does not exist")
                            
                            # if you need to send email
                            
                        else:
                            error = _("price not correct")
                    else:
                        error = _("product does not exist")
            else:
                error = _("Duplicate ipn")
    return HttpResponse('ok')





def purchaesd_emails(request):
    # Get all users who have purchased any tool
    user_with_purchased_tools = User.objects.filter(profile__purchased_tools__isnull=False).distinct()
    
    # Get the emails of those users
    emails_of_users_with_purchased_tools = user_with_purchased_tools.values_list('email', flat=True)
    
    context={'emails': emails_of_users_with_purchased_tools}
    return render(request, 'registration/purchased_emails.html', context)
