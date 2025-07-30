from django.shortcuts import render
from django.shortcuts import HttpResponse



# Create your views here.
def my_user_view(request):
    # return HttpResponse("Hii")
    return render(request, 'UserApp/my_user_template.html',{})