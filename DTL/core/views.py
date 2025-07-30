from django.shortcuts import render
from datetime import date

# Create your views here.
# def itpre(request):
#     course_name = "python Django Full Stack"
#     course_duration = "6 months"
#     course_fee = ""

#     course_details = {
#         "cname": course_name,
#         "cduration":course_duration,
#         "cfee":course_fee

#     }

#     return render(request, "core/itpreneur.html",course_details)



def fliter_demo(request):
    context = {
        "name": 'vaishnavi bhonde',
        "student": ['sagar', 'rani','pratik','yogesh'],
        'bio':"",
        "today": date.today(),
        "description": ['red','green','blue'],
        "is_active": "True",
        "color":["red", "green", "blue"]


    }

    return render(request,  "core/itpreneur.html",context)