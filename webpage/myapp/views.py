from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def headerPage(request):
    return render(request, 'header.html')

def basePage(request):
    return render(request, 'base.html')


def RegisterPage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # User is created
            messages.success(request, 'Registration successful! You can now log in.')  # Success message
            return redirect('login')  # Redirect to login page after successful registration
        else:
            # Add debugging information
            messages.error(request, 'Registration failed. Please check the provided information.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect authenticated users to the home page

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or another page
        else:
            messages.error(request, 'Invalid username or password')  # Show error message

    return render(request, 'login.html')


@login_required  # Ensure only authenticated users can access this view
def HomePage(request):
    return render(request, 'home.html')


def LogoutPage(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')  # Show logout success message
    return redirect('login')

def AboutPage(request):
    return render(request, 'about.html')
    
def ContactPage(request):
    return render(request, 'about.html')

