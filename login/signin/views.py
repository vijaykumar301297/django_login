from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode

from .models import Signup
from django.core.mail import send_mail
from login import settings


# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        fullname = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(email=email):
            messages.error(request, 'Email Already available, kindly click on login or reset the password')

        if User.objects.filter(username=username):
            messages.error(request, 'username Already available,  kindly click on login or reset the password')

        myuser = User.objects.create_user(username=username, first_name=fullname, email=email, password=password)
        myuser.save()

        subject = "Login message"
        message = "Hello " + myuser.username + ','
        from_email = settings.EMAIL_HOST
        to_user = [myuser.email]
        send_mail(subject, message, from_email, to_user, fail_silently=True)

        messages.success(request, "Account created")
        return redirect('login')

    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            userdata = user.username
            return render(request, 'home.html', {username: userdata})
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username Already available,  kindly click on signup or reset the password')
            else:
                messages.error(request, 'Bad Credential')
            return redirect('login')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
