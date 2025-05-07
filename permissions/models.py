from django.db import models
from django.utils import timezone

class Permission(models.Model):
    student_name = models.CharField(max_length=100)
    parent_email = models.EmailField()
    outing_reason = models.TextField(max_length=200, blank=True)
    outing_time = models.DateTimeField()
    return_time = models.DateTimeField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    requested_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student_name} - {'Approved' if self.approved else 'Pending'}"