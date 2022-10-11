from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from apps.users.serializers import UserSerializer, GroupSerializer


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


def profile_page_m(request):
    return render(request, "profile_page_m.html")


def forgot_p(request):
    return render(request, "forgot_p.html")


def create_a(request):
    return render(request, "create_a.html")


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
