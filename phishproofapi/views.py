from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Classes, Challenges

# Create your views here.
def home(request):
    return render(request, 'phishproofapi/home.html')
def class_list(request):
    class_list = Classes.objects.all()
    return render(request, 'phishproofapi/class_list.html', {'class_list': class_list})

def class_description(request, pk):
    classes = get_object_or_404(Classes, pk=pk)
    return render(request, 'phishproofapi/class_description.html', {'classes': classes})

def challenge_list(request):
    challenge_list = Challenges.objects.all()
    return render(request, 'phishproofapi/challenge_list.html', {'challenge_list': challenge_list})

def challenge_description(request, pk):
    challenges = get_object_or_404(Classes, pk=pk)
    return render(request, 'phishproofapi/challenge_description.html', {'challenges': challenges})

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
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
        
    return render(request, 'phishproofapi/login.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'phishproofapi/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

def enroll_class(request, class_id):
    if not request.user.is_authenticated:
        return redirect('login')
    classes = get_object_or_404(Classes, id=class_id)
    classes.students.add(request.user)
    classes.save()
    return redirect('class_list')

def start_challenge(request, challenge_id):
    if not request.user.is_authenticated:
        return redirect('login')
    challenges = get_object_or_404(Challenges, id=challenge_id)
    challenges.students.add(request.user)
    challenges.save()
    return redirect('challenge_list')