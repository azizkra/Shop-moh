from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout
from django.contrib import messages
from .form import RegistrationForm, ContactForm, UserEditForm, ProfileEditForm
from .models import Profile
from tools.models import Tool
from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
import os
# Create your views here.

def register(request):
    page = 'register'
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = new_user.username.lower()
            # user.set_password(form.cleaned_data['password1'])
            new_user = form.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            messages.success(request, _('Registration successfully you can now login-in'))
            return redirect('login_view')
        else:
            messages.error(request, _('Something error, try again later'))
            return redirect('register')
    else:
        form = RegistrationForm()
    
    context={'form':form, 'page':page}
    return render(request, 'registration/register.html', context)


def user_login(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, _('Login-in successfully'))
            return redirect('/')
        else:
            messages.error(request, _('Invalid username or password'))
            return redirect('login_view')
    return render(request, 'registration/login.html', {'page':page})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Updating profile successfully'))
        else:
            messages.error(request, _('Somthing want wrong'))
            return redirect('profile')
    else:
        user_form = user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user)
    
    context={
            'user_form':user_form,
            'profile_form':profile_form,
        }
    return render(request, 'registration/edit_profile.html', context)

@login_required
def edit_profile(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    purchased_tools = user_profile.purchased_tools.all()
    
    # Set default form instances for GET request or invalid POST data
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST, instance=request.user )
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Redirect to a success page after successful form submission
            return redirect('edit_profile')
        
    context={
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user,
        'purchased_tools': purchased_tools
    }
    return render(request, 'registration/edit_profile.html', context)

@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #تحديث جلسة المستخدم بكلمة المرور الجديدة للحفاظ على حالة المصادقة للمستخدم
            messages.success(request, _('Your password changed successfully'))
            return redirect('/')
    else:
        form = PasswordChangeForm(request.user)
        
    return render(request, 'registration/change_password.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, _('See you ^_^'))
    return redirect('login_view')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Send email
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                'your_email@example.com',
                ['recipient@example.com'],
                fail_silently=False,
            )
            messages.success(request, _('Your message sent successfully'))
            return redirect('success')  # Redirect to success page
        
        else:
            messages.error(request, 'Try later please')
            return redirect('contact')
    else:
        
        form = ContactForm()
    return render(request, 'registration/contact.html', {'form': form})


def success_view(request):
    return render(request, 'registration/success.html')


def trems_view(request):
    return render(request, 'other/trems.html')
    
def about_view(request):
    return render(request, 'other/about.html')

def cancel_view(request):
    return render(request, 'other/cancel.html')

def success(request):
    return render(request, 'other/success.html')


def download_exe(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    
    if not tool.upload_tool:
        raise Http404(_('.exe file not found'))
    
    
    # Check if the user is the owner of the tool or has purchased it
    if request.user == tool.username or tool.is_purchased_by(request.user):
        # Allow the user to download the tool
        file_path = tool.upload_tool.path
        try:
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                return response
        except FileNotFoundError:
            raise Http404(_('File not found'))
    else:
        # Redirect or show an error message indicating that the tool is not accessible
        # to the user
        error_message= _('You do not have permission to download this tool.')
        context={'error_message':error_message}
        return render(request, 'registration/profile_edit.html', context)
    
    
    

