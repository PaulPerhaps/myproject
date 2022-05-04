from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/login')
        else:
            messages.success(request, 'Invalid Credentials.')
            return redirect('/login')
    else:
        return render(request, "login_page.html")


def logout_page(request):
    logout(request)
    return redirect('/login')


def home_page(request):
    return render(request, "home_page.html")
