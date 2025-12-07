from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Classes

# Create your views here.
def home(request):
    return render(request, 'phishproofapi/home.html')
def class_list(request):
    class_list = Classes.objects.all()
    return render(request, 'phishproofapi/class_list.html', {'class_list': class_list})

def class_description(request, pk):
    classes = get_object_or_404(Classes, pk=pk)
    return render(request, 'phishproofapi/class_description.html', {'classes': classes})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')
        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, "Account created successfully.")
        return redirect('login')
    
    return render(request, 'phishproofapi/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
        
    return render(request, 'phishproofapi/login.html')