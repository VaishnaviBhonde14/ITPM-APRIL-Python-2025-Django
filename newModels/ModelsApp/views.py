from django.shortcuts import render
from .models import new_Student

# Create your views here.
def home(request):
    student = new_Student.objects.create(
        stuId = 101(unique=True),
        name = "Ram joshi",
        # age = 36,
        email = "ram19@32gmail.com",
        addr = "Pune"

    )

    return render(request, "ModelsApp/home.html", {"student" : student})

