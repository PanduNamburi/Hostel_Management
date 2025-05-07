from django.contrib import admin
from .models import Permission
from django.core.mail import send_mail

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'outing_time', 'return_time', 'approved', 'requested_at')
    list_filter = ('approved',)
    actions = ['approve_permissions']

    def approve_permissions(self, request, queryset):
        for permission in queryset:
            if not permission.approved:
                permission.approved = True
                permission.save()
                self.send_approval_email(permission)
    approve_permissions.short_description = "Approve selected permissions"

    def save_model(self, request, obj, form, change):
        if change:
            old_obj = Permission.objects.get(pk=obj.pk)

            # If outing just got approved
            if not old_obj.approved and obj.approved:
                self.send_approval_email(obj)

            # If return time was just added
            if not old_obj.return_time and obj.return_time:
                self.send_return_email(obj)

        super().save_model(request, obj, form, change)

    def send_approval_email(self, permission):
        subject = f"{permission.student_name} Outing Approved"
        message = (
            f"Your student {permission.student_name}'s outing request has been approved.\n\n"
            f"Reason: {permission.outing_reason}\n"
            f"Outing Time: {permission.outing_time}"
        )
        send_mail(subject, message, 'pandunamburi18@gmail.com', [permission.parent_email])

    def send_return_email(self, permission):
        subject = f"{permission.student_name} Returned to Hostel"
        message = (
            f"Your student {permission.student_name} has returned to the hostel.\n"
            f"Return Time: {permission.return_time}"
        )
        send_mail(subject, message, 'pandunamburi18@gmail.com', [permission.parent_email])
