from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
import math, random 
from django.core.mail import send_mail
from django.conf import settings 
from django.http import HttpResponse
from pprint import pprint 
from django.contrib.auth import views as auth_views
from django.db import connection
from django.contrib.auth.models import User

# Create your views here.
#def register(request):
 #   return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['psw']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/") 
        else:
            messages.error(request," * Invalid User ID") 
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
        special_symbol=['$', '@', '#', '%']

        if psw1==psw2:
             if User.objects.filter(username=username).exists():
                 messages.info(request," * Username Taken!!")
                 return redirect('register')
# checks if the email exists or not..
             elif User.objects.filter(email=email).exists():
                 messages.info(request," * Email Taken!!")
                 return redirect('register')
# checks if the length of the password is not less the 8 characters             
             elif len(psw1)<8:
                 messages.info(request,"* Short password..!")
                 messages.info(request,"It must be alteast 8 characters.")
                 return redirect("register")
# checks if it has the special characters is present in the password or not
             elif not any(char in special_symbol for char in psw1):
                 messages.info(request,"* Password must contain special characters like '$', '@', '#', '%'")
                 return redirect("register")
# checks if the password has some upper case letters or not
             elif not any(char.isupper() for char in psw1):
                 messages.info(request,"* Password should have at least one uppercase letter")
                 messages.info(request,"For example:This@1234")
                 return redirect("register")
             
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
    return render(request,'forgot_pass.html')

otp = ""
email = ""
def mail(request):
    global email
    if request.method == 'POST' :
        email=request.POST['e-mail']
        if User.objects.filter(email=email).exists():
            #user = User.objects.filter(email=email)
            #user_name = user.first_name
            digits="0123456789"
            global otp
# generating otp
            for i in range(4):
                otp += digits[math.floor(random.random() * 10)]
    #return otp


# **********************************************************e-mail********************************

            subject = "OTP for changeing password BLISS ENTERTAINMENT"  
    #print(time)
            msg = "This is a system generated mail.. Please do not send any mail in this... Your OTP for validation is = " + otp 
            to  = email
            res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
            if(res == 1):
                messages.info(request," * Mail sent.!!") #% user_name   %s
                pprint(otp)
                return render(request,"otp.html")
            else:
                messages.info(request," * Mail could not sent.!!")
                email = ""   
                return render(request,"forgot_pass.html")
        else:
            messages.info(request,"* NO such User Exists..!!")
            email = ""
            return render(request,"forgot_pass.html")


def change_pass(request):
    if request.method == 'POST' :
        temp_otp=request.POST['otp']
        global otp
    pprint(otp)
    if otp==temp_otp:
        otp = ""
        return redirect('new_pass')
    else:
        messages.info(request,"OTP Does not match!!")
        return render(request,"otp.html") 



def new_pass(request):
    global email
    if request.method == 'POST' :
        new_pas=request.POST['new_pass']
        con_pas=request.POST['con_pass']
        
        if new_pas==con_pas:
            special_symbol=['$', '@', '#', '%']
            if len(new_pas)<8:
                messages.info(request,"* Short password..!")
                messages.info(request,"It must be alteast 8 characters.")
                return redirect('new_pass')
# checks if it has the special characters is present in the password or not
            elif not any(char in special_symbol for char in new_pas):
                messages.info(request,"* Password must contain special characters like '$', '@', '#', '%'")
                return redirect('new_pass')
# checks if the password has some upper case letters or not
            elif not any(char.isupper() for char in new_pas):
                messages.info(request,"* Password should have at least one uppercase letter")
                messages.info(request,"For example:This@1234")
                return redirect('new_pass')
        #u = User.objects.filter(email=email).update(password=new_pass) 
            else:
                user = User.objects.get(email=email)
                user.set_password(new_pas)          
                user.save()
                messages.info(request,"* password updated!!")
                return redirect('login')
        else:
            messages.info(request,"* password Do Not Match!!")
            return redirect('new_pass')
    else:
       # messages.info(request,"password do not match")
        return render(request,'new_password.html')
    