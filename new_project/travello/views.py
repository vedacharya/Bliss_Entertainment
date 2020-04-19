from django.shortcuts import render,redirect
from django.http import HttpResponse  
from django.conf import settings 
from django.contrib import messages
from django.contrib.auth.models import User, auth
from pprint import pprint
from django.db.models import Count,Sum
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
import math, random 
from .models import *


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['psw']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("service")
        else:
            messages.info(request," * Invalid User ID")
            return redirect("login")
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
   if request.method == 'POST' :
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        psw1=request.POST['psw1']
        psw2=request.POST['psw2']
        limit = 8
        if psw1==psw2:
             if User.objects.filter(username=username).exists():
                 messages.info(request," * Username Taken!!")
                 return redirect('register')
             elif (psw1<limit):
                 messages.info(request,'* Password must be of atleast 8 characters..!')
                 return redirect('register')
             elif User.objects.filter(email=email).exists():
                 messages.info(request," * Email Taken!!")
                 return redirect('register')
             else:
                 user = User.objects.create_user(username=username, password=psw1, email=email, first_name=first_name, last_name=last_name)
                 user.save();
                 print('User created')
                 messages.info(request," * USER CREATED...!!")
                 return redirect('login')
        else:
            messages.info(request," * Password not matching.. .!")
            return redirect('register')
   else:
      return render(request,'register.html')


def forgot_pass(request):
    return render(request, 'forgot_pass.html')


def mail(request):
    if request.method == 'POST' :
        email=request.POST['e-mail']

    digits="0123456789"
    otp=""

# generating otp
    for i in range(4):
        otp += digits[math.floor(random.random() * 10)]
    


# **********************************************************e-mail********************************

    subject = "OTP for changeing password BLISS ENTERTAINMENT"  
    print(time)
    msg = "This is a system generated mail.. Please do not send any mail in this... Your OTP for validation is = " + otp 
    to  = email
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        messages.info(request," * Mail sent.!!")  
    else:  
        messages.info(request," * Mail could not sent.!!")  
    return render(request,"otp.html") 





#***********************************************************************************************************************

def eve_register(request):
    if request.method == 'POST' :
        event_name=request.POST['event_name']
        category = request.POST['category']
        sub_category = request.POST['sub_category']
        #Country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        pin_code = request.POST['pin_code']
        landmark = request.POST['landmark']
        st_date= request.POST['st_date']
        st_time = request.POST['st_time']
        end_date = request.POST['end_date']
        end_time = request.POST['end_time']
        describe = request.POST['description']
        last_datebooking = request.POST.get('last_datebooking')
       # eve_photo = request.POST.get('eve_photo', False)
        pay_type = request.POST.get('pay_type')
        facebook = request.POST['facebook']
        insta = request.POST['insta']
        youtube = request.POST['youtube']
        twitter = request.POST['twitter']
        longitude = 0
        latitude = 0
        event_like = 0

        sub_cate = EventSubCategory.objects.get(event_sub_category_name=sub_category)
        f_sub_cate = sub_cate.event_sub_category_id
        pprint("########################333")
        #pprint(eve_photo)

        pprint(f_sub_cate)
        tcity=City.objects.get(city_name=city)
        user = AuthUser.objects.get(id=request.user.id)
        #pprint(user_id)
        #print(eve_photo)

        pprint("########################333")

        uplaoded_file = request.FILES['image']
        print(uplaoded_file.name)
        print(uplaoded_file.size)
        na = uplaoded_file.name
        fs = FileSystemStorage(location='/media/event_pics')
        p_name = fs.save(uplaoded_file.name, uplaoded_file)
        url = fs.url(p_name)
        print(url)



        pprint("########################333")
        location = Location(full_address=address, landmark=landmark, postal_code=pin_code, longitude=longitude, latitude=latitude, city=tcity)
        location.save()
        loc_id = Location.objects.latest('location_id')
        location = loc_id.location_id
        event = Event(evemt_name=event_name, location_location_id=location, event_image=url , event_description=describe, event_start_date=st_date, event_end_date=end_date, event_time=st_time,ticket_details_type = 0, end_time=end_time, last_booking_date=last_datebooking, facebook_link=facebook, instagram_link=insta, twitter_link=twitter, linkedin_link=youtube, event_sub_category=sub_cate, auth_user=user)
        event.save()
        messages.info(request,"* Event added..!!")
    return redirect('all_event')    





def index(request):
     events = Event.objects.all()
     images = EventImage.objects.all().filter(event_id__in = [event.event_id for event in events])
    #eve =details =EventImage.objects.all().raw('SELECT * FROM event_image WHERE event_id = ' + str(event.event_id))
     states =State.objects.all()
     category = EventCategory.objects.all()
    
     return render(request,'index.html',{'events':events,'images':images,'states':states, 'category':category})

def contact(request):
   return render(request,'contact.html')

def describe(request):
    return render(request,'about.html')

def destinations(request):
    return render(request,'destinations.html')


def service(request):
    if request.user.is_authenticated:
         events = Event.objects.all().filter(auth_user_id=request.user.id)
         event_count = 0
         event_count = len(events)
         pprint(event_count)
         event_ids = []
         for event in events:
            event_ids.append(event.event_id)

         tickets = []

    # bookings = BookingMaster.objects.all().filter(event_event_id__in = event_ids)
         bookings = BookingMaster.objects.all().filter(event_event_id__in = [event.event_id for event in events])
         total_tickets = TicketTypeMaster.objects.all().filter(event_id__in = [event.event_id for event in events])
         total_earning = 0
         for booking in bookings:
             total_earning += booking.total_charges
         


    # total tickets for sold by user as per the events ...


         total_ticket = 0
         for ticket in total_tickets:
             total_ticket += ticket.ticket_sold

         pprint('\n\n\n\n')
         pprint('total_ticket')
         pprint(total_ticket)
         pprint('\n\n\n\n')

         return render(request,'service.html',{'event_count':event_count, 'sales':sales, 'total_earning':total_earning, 'total_ticket':total_ticket})    
    # event_count =Event.objects.filter(auth_user_id=request.user.id).count()
    else:
        messages.info(request,'* You need to Login First')
        return login(request)





    # #total_sales =BookingMaster.objects.annotate(sales=Sum('total_charges'))
    # sales =BookingMaster.objects.all().raw('SELECT SUM("total_charges") FROM booking_master WHERE event_id = ' + 'eventcount')

    # if request.user.is_authenticated:
    #     return render(request,'service.html',{'event_count':event_count, 'sales':sales})
    # else:
    #     messages.info(request,'* You need to Login First')
    #     return login(request)

def sales(request):
    records = BookingMaster.objects.all()
    events = Event.objects.all().filter(auth_user_id=request.user.id)
    return render(request,'table.html',{'records':records, 'events':events})

###############################################################################################################################

def request_sales(request):
    if request.method == 'POST' :
        event_name=request.POST['event']
    eve = Event.objects.get(evemt_name=event_name)
    eve_id =eve.event_id
    pprint(eve_id)
    events = Event.objects.all().filter(auth_user_id=request.user.id)
    records = BookingMaster.objects.filter(event_event_id=eve_id)
    if not records:
        messages.info(request,'No sales recorded...!!')
        return render(request,'table.html',{'records':records, 'events':events})
    else:
        return render(request,'table.html',{'records':records, 'events':events})



###############################################################################################################################

def profile(request):
    details =OrganizerProfile.objects.all().filter(auth_user_id=request.user.id)
    
    #details =OrganizerProfile.objects.all().raw('SELECT * FROM organizer_profile WHERE auth_user_id = ' + str(request.user.id))
    return render(request,'profile.html',{'details':details})
##########################################################################################################################3
         # this is for organiser page_edit 
         # it will check if the data is aready there or not,,, 
         # if it exits then, it will show data for edit, else will not.
         
def profile_edit(request):
    user = AuthUser.objects.get(id=request.user.id)
    user_data = OrganizerProfile.objects.all().filter(auth_user_id=request.user.id)
    if not user_data:
        return render(request,'profile_edit.html')
    else:
        return render(request,'profile_edit.html', {'user_data':user_data})

###########################################################################################################################

def all_event(request):
    event = Event.objects.all().filter(auth_user_id=request.user.id)
    types = EventSubCategory.objects.all()
    return render(request,'event_page.html',{'event':event, 'types':types})

def event_form(request):
    #Fetching all the events

    event_category = EventCategory.objects.all()
    event_sub_category = EventSubCategory.objects.all()
   

    #fetching locaton........

    country = Country.objects.all()
    state = State.objects.all()
    city = City.objects.all()

    return render(request,'form_event.html',{'event_category':event_category, 'event_sub_category':event_sub_category, 'country':country, 'state':state, 'city':city}) 


   