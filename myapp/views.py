from django.shortcuts import render
from  django.http import HttpResponse
def home(request):
    return HttpResponse("heartly welcome to India")
def homeNew(request):
    return HttpResponse("Thankyou for visiting INDIA")

# Create your views here.
