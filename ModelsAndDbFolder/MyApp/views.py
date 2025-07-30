from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    # students = Student.objects.all()

    # students = Student.objects.create(
    #     name = "Joy Doe",
    #     age = 20,
    #     email = "abc@gmail.com"
    # )
    # students = Student.objects.create(
    #     name = "ram joy",
    #     age = 22,
    #     email = "pqr@gmail.com"
    # )


    # students = Student.objects.all()
    # return render(request, 'MyApp/home.html', {'students' : [students]})


#    if not Student.objects.exists():
     Student.objects.create(
        name = "Joy Doe",
        age = 20,
        email = "abc@gmail.com"
     )
     Student.objects.create(
        name = "ram joy",
        age = 22,
        email = "pqr@gmail.com"
     )


    #fetching all students
     students = Student.objects.all()
     return render(request, 'MyApp/home.html', {'students' : students})


