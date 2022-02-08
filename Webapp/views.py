from django.shortcuts import render
from datetime import datetime
from Webapp.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'maintainance.html')

def contact_us(request):
    if request.method =="POST":
        First_Name=request.POST.get('First_Name')
        Last_Name=request.POST.get('Last_Name')
        Email=request.POST.get('Email')
        Desc=request.POST.get('Desc')
        if len(First_Name)<3 or len(Last_Name)<3 or len(Desc)>=200 or Email=="":
            messages.warning(request,'Fill the form correctly')
        else:
            data=Contact(First_Name=First_Name,Last_Name=Last_Name,Email=Email,Desc=Desc,Date=datetime.today())
            data.save()
            messages.success(request,'Message Received Successfully')
    return render(request,'contact_us.html')

def Profile(request):
    return render(request,'resume.html')



