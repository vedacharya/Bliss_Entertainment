from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('describe',views.describe,name='describe'),
    path('destinations',views.destinations,name='destinations'),
    path('service',views.service,name="service"),
    path('sales',views.sales,name="sales"),
    path('profile',views.profile,name="profile"),
    path('profile_edit',views.profile_edit,name="profile_edit"),
    path('all_event',views.all_event,name="all_event"),
    path('event_form',views.event_form,name="event_form"),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('forgot_pass',views.forgot_pass,name='forgot_pass'),
    path('mail',views.mail,name='mail'),
    path('request_sales',views.request_sales,name='request_sales'),
    path('eve_register',views.eve_register,name='eve_register'),
    #path('change_pass',views.change_pass,name='change_pass'),



]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)