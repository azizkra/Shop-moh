from django.urls import path
from .views import (
        display_tool,
        add_Tool,
        update_Tool,
        delete_Tool,
    )

urlpatterns = [
    path('', display_tool, name="display_tool"),
    path('add-tool/', add_Tool, name="add_tool"),
    path('update-Tool/<str:pk>', update_Tool, name="update_tool"),
    path('delete-Tool/<str:pk>', delete_Tool, name="delete_tool"),
    
]


