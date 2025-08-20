from django.shortcuts import render,redirect
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import RegistrationForm
import random
from django.core.mail import send_mail
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)  # Generate a refresh token for the user
    # Return a dictionary containing the refresh and access tokens
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

def register(request):
    if request == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            otp=str(random.rndint(100000, 999999))  # Example of generating a random number
            request.session['user_data'] = form.cleaned_data  # Store the OTP in the session
            request.session['otp'] = otp   # Store the OTP in the session
        
            send_mail(
                'OTP Verification',
                f'you OTP is {otp}',
                'bvaishanvi871@gmail.com',
                [form.cleaned_data['email']],   # Send to the user's email
            )
            return redirect('verify_otp')   # Redirect to OTP verification page
        else:
            form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})
    
def verify_otp(rqeuset):
    if rqeuset.method == 'POST':
            if rqeuset.POST.get('otp') == rqeuset.session.get('otp'):
                data = rqeuset.session.get('user_data')
                user = CustomUser.objects.create_user(
                       email = data['email'],
                       role = data['role'],
                       password = data['password'],
                )
                messages.error =  (rqeuset,"Registration successful. you can now log in.")
                return redirect('login')
            else:
                messages.error = (rqeuset,"Invaild OTP, Please try again.")
    return render(rqeuset, 'user/verify_otp.html')

    
def login(request):
    if request.method == 'POST':
        user = authenticate(request, email=request.POST['email'],password = request.POST['password'])
        if user:
            login(request, user) # Log the user in
            request.session['access_token'] = get_token_for_user(user)['access']   # Store the access token in the session
            return redirect('dashboard')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Inavail email or password. please try again.')
    return render(request, 'users/login.html')
 
@login_required  # Ensure the user is logged in to access the dashboard this is a decorator that checks if the user is authenticated
def dashboard(request):
    return redirect(request, 'users/dashbaord.html', {'role': request.user.role})

def logout(request):
    logout(request)  # Log the user out
    return redirect('login') # Redirect to the login page after logout

def forgot_password(request):
    if request.method == 'POST':
        try:
            user = CustomUser.object.get(email=request.POST['email'])
            otp = str(random.rendint(100000, 999999))  # Generate a random OTP
            request.session['forgot_email'] = user.email  # Store the OTP in the session
            request.session['forgot_otp'] = otp # Store the OTP in the session
            
            send_mail('Password Reset OTP',
                      f'Your OTP for password reset is {otp}',
                      'bvaishanvi871@gamil.com', # Replace with your email
                      [user.email])
            return redirect('verify_forgot_otp') # Redirect to OTP verification page
        except CustomUser.DoesNotExist:
            messages.error(request, "Email not found. please try again.")
    return render(request, 'user/forgot_password.html')


def verify_forgot_otp(request):
    if request.method == 'POST':
        if request.POST.get('otp') == request.session.get('forgot_otp'):
            if request.POST.get('new_password') == request.POST.get('confirm_password'):
                user = CustomUser.objects.get(email=request.session.get('forgot_email'))
                user.set_password(request.POST.get('new_password'))
                user.save()
                messages.success(request, "Password reset successfut. You can now log in.")
            else:
                messages.error(request, "Password do not match. Please try again")
        else:
            messages.error(request, "Invaild OTP. Please try again.")
    return render(request, 'users/verify_forgot_otp.html')
