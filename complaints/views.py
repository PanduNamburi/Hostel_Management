from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Complaint
from .forms import ComplaintForm

# Redirect to complaints list after login
@login_required
def home_redirect(request):
    return redirect('complaint_list')


# ✅ View to list complaints
@login_required
def complaint_list(request):
    if request.user.is_staff:
        complaints = Complaint.objects.all()  # Wardens see all
    else:
        complaints = Complaint.objects.filter(user=request.user)  # Students see their own
    return render(request, 'complaints/list.html', {'complaints': complaints})


# ✅ View to submit a new complaint
@login_required
def submit_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect("complaint_list")
    else:
        form = ComplaintForm()
    return render(request, "complaints/submit_complaint.html", {"form": form})


# ✅ View to update complaint status (for wardens)
@login_required
@login_required
def update_complaint_status(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)

    if request.user.is_staff:
        if request.method == "POST":
            status = request.POST.get("status")
            complaint.status = status
            complaint.save()
            return redirect("complaint_list")

    return render(request, "complaints/update_status.html", {"complaint": complaint})

