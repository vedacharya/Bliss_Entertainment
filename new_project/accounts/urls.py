from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('forgot_pass',views.forgot_pass,name='forgot_pass'),
    path('mail',views.mail,name='mail'),
    path('change_pass',views.change_pass,name='change_pass'),
    path('new_pass',views.new_pass,name='new_pass'),
]