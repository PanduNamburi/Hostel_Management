from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from complaints.models import Complaint
from django.contrib.auth.models import User
from .forms import RegisterForm  # Updated to import RegisterForm from forms.py

# User registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)  # Use RegisterForm instead of CustomUserCreationForm
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after successful registration
            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')  # Redirect to the home page or dashboard after successful registration
    else:
        form = RegisterForm()  # Use RegisterForm
    return render(request, 'users/register.html', {'form': form})

# Custom login view (you can also use Django's built-in LoginView if needed)
def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use username instead of email for login
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'users/login.html')

# Home view for authenticated users
def home(request):
    if request.user.is_authenticated:
        complaints = Complaint.objects.all() if request.user.is_staff else Complaint.objects.filter(user=request.user)
        total = complaints.count()
        pending = complaints.filter(status='pending').count()
        resolved = complaints.filter(status='resolved').count()

        return render(request, 'dashboard.html', {
            'total': total,
            'pending': pending,
            'resolved': resolved,
            'is_warden': request.user.is_staff,
            'complaints': complaints[:5],  # latest 5
        })
    return render(request, 'home.html')

# Dashboard view for authenticated users
@login_required
def dashboard(request):
    complaints = Complaint.objects.all() if request.user.is_staff else Complaint.objects.filter(user=request.user)
    total = complaints.count()
    pending = complaints.filter(status='pending').count()
    resolved = complaints.filter(status='resolved').count()

    return render(request, 'dashboard.html', {
        'total': total,
        'pending': pending,
        'resolved': resolved,
        'is_warden': request.user.is_staff,
        'complaints': complaints[:5],  # latest 5
    })

# Complaint list view for authenticated users
@login_required
def complaint_list(request):
    complaints = Complaint.objects.all() if request.user.is_staff else Complaint.objects.filter(user=request.user)
    return render(request, 'list.html', {'complaints': complaints})
