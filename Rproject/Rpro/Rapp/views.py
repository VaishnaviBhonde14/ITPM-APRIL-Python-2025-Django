from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("<b>Hello, my name is vaishnavi</b>")