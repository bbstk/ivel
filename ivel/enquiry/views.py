from django.shortcuts import render
from django.http import HttpResponse
from enquiry.models import Enquiry
import datetime

def index(request):
    return render(request,'index.html')

def add(request):
    new_enquiry=Enquiry(name=request.POST['name'],email=request.POST['email'],phone=request.POST['phone'],location=request.POST['location'],description=request.POST['description'],category="general")
    new_enquiry.save()
    return render(request,'index.html')