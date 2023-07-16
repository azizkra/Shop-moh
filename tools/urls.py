from django.urls import path
from .views import (
        display_tool,
        tool_detail,
        add_Tool,
        update_Tool,
        delete_Tool,
        search_tool,
        
        # -- Coinbase_Payment -- 
        Coinbase_Payment,
        coinbase_postback
    )

urlpatterns = [
    path('', display_tool, name="display_tool"),
    path('tool/<slug:slug>/', tool_detail, name="tool_detail"),
    path('add-tool/', add_Tool, name="add_tool"),
    path('update-Tool/<str:pk>', update_Tool, name="update_tool"),
    path('delete-Tool/<str:pk>', delete_Tool, name="delete_tool"),
    
    
    path('search/', search_tool, name='search_tool'),
    
    path('coinbase_payment/<int:id>/', Coinbase_Payment, name="Coinbase_Payment"),
    path('coinbase_postback/', coinbase_postback, name="coinbase_postback"),
    
]


