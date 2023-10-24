from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile


# Create your views here.

def index0(request):
    if request.user.is_authenticated:
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        return render(request, 'user_index0.html', {'profile': profile})
    else:
        return render(request, 'index0.html')

def main(request):
    return render(request, 'main.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['loginUsername']
        password = request.POST['loginPassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index0')  # Redirect to your desired page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['registerUsername']
        password = request.POST['registerPassword']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
    return render(request, 'register.html')

def about_view(request):
    return render(request, 'about.html')

def todo_view(request):
    return render(request, 'todo.html')

