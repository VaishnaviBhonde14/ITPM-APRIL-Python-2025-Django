from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Hello to all")
def hello(request):
    return HttpResponse("<h1>Welcome to word</h1>")
