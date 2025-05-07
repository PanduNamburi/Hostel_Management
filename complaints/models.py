from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ("Food", "Food Issue"),
        ("Room", "Room Issue"),
        ("Pest", "Pest Problem"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    urgent = models.BooleanField(default=False)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    
    # ✅ New Field
    estimated_days = models.PositiveIntegerField(null=True, blank=True, help_text="Estimated number of days to resolve")

    def __str__(self):
        return f"{self.category} - {self.user.username} ({self.status})"

# ✅ Add Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
