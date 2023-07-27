from django import forms
from .models import Tool ,type_tool


class ToolForm(forms.ModelForm):

    class Meta:
        model = Tool
        fields = [
            'tool_name',
            'image',
            'price',
            'token',
            'upload_tool',
            'quantity',
            'type_of_tool',
        ]