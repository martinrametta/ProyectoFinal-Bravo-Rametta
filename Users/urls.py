from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', login_request, name='Login'),

    path('register/', register, name='Register'),

    path('logout/', LogoutView.as_view(template_name='Users/logout.html'), name='Logout'),   
    
    path('editProfile/', editProfile, name='editProfile'),
   
    path('profile/<user_id>', profile, name='Profile'),
   
    path('edit/avatar/', editAvatar, name='editAvatar'),
]