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
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, "home_page.html")


def profile_page(request):
    return render(request, "profile_page.html")


def gallery_page(request):
    return render(request, "gallery_page.html")


def zoom(request):
    return render(request, "zoom.html")


def about(request):
    return render(request, "about.html")
