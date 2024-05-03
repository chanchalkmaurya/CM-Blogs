from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #messages.success(request, (request, username, password))
        # authenticate user now
        user = authenticate(request, username=username, password=password)
        
        # login
        if user is not None:
            login(request, user)
            messages.success(request, "User Loggedin Successfully")
            return redirect('index')
        else:
            messages.success(request, ("Invalid username/password. try Again."))
            return redirect('login')
    
    context = {
        'title': 'Login page',
    }
    return render(request, 'authenticationpages/login.html', context)


@api_view(['GET', 'POST'])
def register_view(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("User Registered Successfully, Enter Credential to Login"))
            return redirect('login')
        
    context = {
        'title': 'Registration page',
        'form': form
    }
    return render(request, 'authenticationpages/register.html', context)

@api_view(['GET'])
def logout_view(request):
    if request.method == "GET":
        logout(request)
        messages.success(request, "User Logged Out Successfully")
        return redirect('index')
    