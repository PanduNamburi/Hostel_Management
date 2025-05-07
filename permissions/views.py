from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils import timezone
from .models import Permission
from .forms import PermissionForm


def request_permission(request):
    if request.method == 'POST':
        form = PermissionForm(request.POST)
        if form.is_valid():
            permission = form.save()
            return render(request, 'permissions/success.html', {'permission': permission})
    else:
        form = PermissionForm()
    return render(request, 'permissions/request_permission.html', {'form': form})


def outing_permission(request, permission_id):
    permission = get_object_or_404(Permission, id=permission_id)

    if permission.approved and not permission.outing_time:
        permission.outing_time = timezone.now()
        permission.save()

        subject = f"{permission.student_name} Outing Details"
        message = (
            f"Your student {permission.student_name} has gone for an outing.\n"
            f"Reason: {permission.outing_reason}\n"
            f"Time: {permission.outing_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        from_email = 'pandunamburi18@gmail.com'
        to_email = permission.parent_email

        print(f"Sending outing email to: {to_email}")
        send_mail(subject, message, from_email, [to_email])

        return HttpResponse("Outing email sent successfully!")

    return HttpResponse("Outing request not approved or already marked as gone.")


def return_notification(request, permission_id):
    permission = get_object_or_404(Permission, id=permission_id)

    if permission.approved and not permission.return_time:
        permission.return_time = timezone.now()
        permission.save()

        subject = f"{permission.student_name} Has Returned"
        message = (
            f"Your student {permission.student_name} has returned to the hostel.\n"
            f"Return Time: {permission.return_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        from_email = 'pandunamburi18@gmail.com'
        to_email = permission.parent_email

        print(f"Sending return email to: {to_email}")
        send_mail(subject, message, from_email, [to_email])

        return HttpResponse("Return email sent successfully!")

    return HttpResponse("Outing not approved or return already recorded.")


def track_status(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        permissions = Permission.objects.filter(student_name__iexact=student_name).order_by('-requested_at')
        return render(request, 'permissions/track_status_result.html', {
            'permissions': permissions,
            'student_name': student_name
        })
    return render(request, 'permissions/track_status.html')
