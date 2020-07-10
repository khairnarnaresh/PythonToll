from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def hi(request):
    return HttpResponse("This is my home page")

def show(request):
    return render(request,'DEMOAPP/hi.html')
