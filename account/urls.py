from django.urls import path
from .views import (
                        register,
                        user_login,
                        change_password,
                        logout_view,
                        edit_profile,
                        
                        
                        contact_view,
                        success_view,
                        trems_view,
                        about_view,
                        
                        
                        download_exe,
                        
                        cancel_view,
                        success,
                    )

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login_view'),
    path('logout/', logout_view, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change-password/', change_password, name='change_password'),
    
    
    path('contact/', contact_view, name='contact'),
    path('contact/success/', success_view, name='success'),
    
    
    path('trems/', trems_view, name='trems'),
    path('about_view/', about_view, name='about'),
    
    
    path('download-exe/<int:tool_id>/', download_exe, name='download_exe'),
    
    path('cancel/', cancel_view, name='cancel_url'),
    path('success/', success, name='redirect_url'),
]
