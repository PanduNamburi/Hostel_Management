from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from complaints.models import Complaint

from django.shortcuts import render


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect       

def register(request):
    return render(request, 'users/register.html')


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
@login_required
def dashboard(request):
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

    return redirect('home')
@login_required
def complaint_list(request):
    if request.user.is_staff:
        complaints = Complaint.objects.all()
    else:
        complaints = Complaint.objects.filter(user=request.user)

    return render(request, 'list.html', {'complaints': complaints})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def custom_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'warden':
                return redirect('warden_dashboard')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'users/login.html')
