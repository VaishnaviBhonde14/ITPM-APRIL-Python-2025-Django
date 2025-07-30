from django.shortcuts import render
from datetime import date


# Create your views here.
def fliter_demo(request):
    context = {
        "name": 'vaishnavi bhonde',
        "student": ['sagar', 'rani','pratik','yogesh'],
        'bio':"",
        "today": date.today(),
        "description": ['red','green','blue'],
        "is_active": "yes",


    }

    return render(request,  "core/itpreneur.html",context)