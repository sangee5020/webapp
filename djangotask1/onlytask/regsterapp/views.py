from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['userid']
        pasword = request.POST['password']
        user = auth.authenticate(username=username, password=pasword)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        userid = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['passwrd']
        confirm_password = request.POST['cnfpasswrd']
        email = request.POST['email']
        if password == confirm_password:
            if User.objects.filter(username=userid).exists():
                messages.info(request, "username alreadytaken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=userid, first_name=first_name, last_name=last_name,
                                                password=password,
                                                email=email)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request, "password mismatch")
            return redirect('register')
        return redirect('/')

    return render(request, 'register.html')
