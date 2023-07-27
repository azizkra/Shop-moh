from django.urls import path
from .views import (
        display_tool,
        tool_detail,
        add_Tool,
        update_Tool,
        delete_Tool,
        search_tool,
        
        smtp_template,
        sender_template,
        shell_template,
        
        #django_lang
        # switch_language,

        
        # -- Coinbase_Payment -- 
        Coinbase_Payment,
        coinbase_postback,
        
        purchaesd_emails,
    )

urlpatterns = [
    path('', display_tool, name="display_tool"),
    path('tool/<slug:slug>/', tool_detail, name="tool_detail"),
    path('add-tool/', add_Tool, name="add_tool"),
    path('update-Tool/<str:pk>', update_Tool, name="update_tool"),
    path('delete-Tool/<str:pk>', delete_Tool, name="delete_tool"),
    
    
    # display tool
    path('smtp', smtp_template ,name='smtp_template'), 
    path('sender', sender_template ,name='sender_template'),
    path('shell', shell_template ,name='shell_template'),
    
    
    path('search/', search_tool, name='search_tool'),
    
    # path('switch-language/', switch_language, name='switch_language'),
    
    
    path('coinbase_payment/<int:id>/', Coinbase_Payment, name="Coinbase_Payment"),
    path('coinbase_postback/', coinbase_postback, name="coinbase_postback"),
    
    path('purchaesd_emails/', purchaesd_emails, name='purchaesd_emails'),
    
    
]


