from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib import messages
from . import RegisterForm

# Create your views here.
def home(request):
    return render(request, 'base.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,'Regitration successful.')
            return redirect('dashboard')
    else:
        form = RegisterForm()


    return render(request, 'account/register.html', {'form': form})


