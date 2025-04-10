from django.contrib import admin
from .models import Complaint, Notification

admin.site.register(Complaint)
admin.site.register(Notification)  # ✅ Register this model
