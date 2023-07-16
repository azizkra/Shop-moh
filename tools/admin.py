from django.contrib import admin
from .models import Tool

# Register your models here.

@admin.register(Tool)
class toolAdmin(admin.ModelAdmin):
    # fields = ['tool_name', 'image', 'username', 'price', 'upload_tool', 'quantity', 'token','purchased_by']
    search_fields = ['name', 'token']