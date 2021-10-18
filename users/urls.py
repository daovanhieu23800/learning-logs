#define url pattern for user in urls.py
from django.urls import path
#libary for login and logout
from django.contrib.auth.views import LoginView,LogoutView
#libart for registation
# from django.contrib.auth.forms import UserCreationForm
from . import views
app_name = 'users'
urlpatterns = [
    #login page
    path('login/', LoginView.as_view( template_name='users/login.html'), name='login'),
    #logout page
    path('logout/', views.logout_view, name='logout'),
    #registere
    # views.register call the function register in views.py
    path('register/', views.register, name='register'),
]
