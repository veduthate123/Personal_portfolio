from django.shortcuts import render ,redirect
from django.http import HttpResponse
from Auth.models import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password , make_password

from django.core.mail import send_mail
from django.conf import settings


def home(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject'] 
        message = request.POST['message']
        
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        gemail=send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,  
            ['Enter-your-email'],  
            fail_silently=False,  
            )
        
        if gemail :
            messages.success(request, "Your response has been save successfully!.")
        else :
            messages.success(request, "an error occured.")
             
        return redirect(f"/#contact")
    return render(request,'home.html')
