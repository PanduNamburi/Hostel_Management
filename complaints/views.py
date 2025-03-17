from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Complaint
from .forms import ComplaintForm

# ✅ View to list complaints
@login_required
def complaint_list(request):
    if request.user.is_staff:  # Warden view
        complaints = Complaint.objects.all()
    else:  # Student view
        complaints = Complaint.objects.filter(user=request.user)

    return render(request, "complaints/list.html", {"complaints": complaints})

# ✅ View to submit a new complaint
@login_required
def submit_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user  # Assign logged-in user
            complaint.save()
            return redirect("complaint_list")  # Redirect to list view

    else:
        form = ComplaintForm()

    return render(request, "complaints/submit_complaint.html", {"form": form})

# ✅ View to update complaint status (for wardens)
@login_required
def update_complaint_status(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)

    if request.user.is_staff:  # Only wardens can update status
        if request.method == "POST":
            status = request.POST.get("status")
            complaint.status = status
            complaint.save()
            return redirect("complaint_list")

    return render(request, "complaints/update_status.html", {"complaint": complaint})
