from django.contrib import admin
from .models import *
# Register your models here.
class AuthUser_admin(admin.ModelAdmin):
    list_display=['first_name','last_name','username','is_superuser','email']
admin.site.register(AuthUser,AuthUser_admin)

    

# event models


class Name_count(admin.ModelAdmin):
    list_display=['country_id','country_name']
admin.site.register(Country,Name_count)

class country_state(admin.ModelAdmin):
    list_display=['state_id','state_name','country']
admin.site.register(State,country_state)

class state_city(admin.ModelAdmin):
    list_display=['city_id','city_name','state']
admin.site.register(City,state_city)

class city_address(admin.ModelAdmin):
    list_display=['location_id','full_address','landmark','postal_code','longitude','latitude','city']
admin.site.register(Location,city_address)

#----------- Event Models---------------->
admin.site.register(EventImage)
admin.site.register(EventCategory)
admin.site.register(EventSubCategory)
admin.site.register(Event)
admin.site.register(TicketTypeMaster)
admin.site.register(BookingDetail)
admin.site.register(BookingMaster)
admin.site.register(PaymentType)
admin.site.register(Customer)
admin.site.register(TicketCancellationMaster)

#------------Hastag Models--------------->
admin.site.register(HashTag)
admin.site.register(EventHasHashTag)

#----------- event admin payment-------->
admin.site.register(EventPayment)

#-----------Enquary for service--------------->

admin.site.register(InquiryCustomer)
admin.site.register(OrganizerProfile)
admin.site.register(OrganizersType)
admin.site.register(Service)
admin.site.register(ServiceType)
admin.site.register(EnquaryMaster)

#----------User like and review--------->
admin.site.register(UserHasLikeMaster)
admin.site.register(UserReviewMaster)
