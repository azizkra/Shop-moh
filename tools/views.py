from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .form import ToolForm
from .models import Tool
# Create your views here.

def display_tool(request):
    tools = Tool.objects.all()
    
    context={'tools':tools}
    return render(request, 'tools/products.html', context)


@staff_member_required
def add_Tool(request):
    if request.method == 'POST':
        form = ToolForm(request.POST, request.FILES)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.username = request.user
            tool.save()
            return redirect('display_tool')
            # return redirect('tool-detail', pk=tool.pk)
    else:
        form = ToolForm()
    
    context={'form':form}
    return render(request, 'tools/tool_form.html', context)

@staff_member_required
def update_Tool(request, pk):
    tool = get_object_or_404(Tool ,id=pk)
    if request.method == 'POST':
        form = ToolForm(request.POST, request.FILES, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('display_tool')
            # return redirect('tool-detail', pk=tool.pk)
    else:
        form = ToolForm(instance=tool)
    context={'form':form}
    return render(request, 'tools/tool_form.html', context)

@staff_member_required
def delete_Tool(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if request.method == 'POST':
        tool.delete()
        return redirect('display_tool')
    
    context={'tool':tool}
    return  render(request, 'tools/delete-product.html', context)