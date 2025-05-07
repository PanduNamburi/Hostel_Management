from django import forms
from .models import Permission

class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['student_name', 'parent_email', 'outing_reason', 'outing_time']
        widgets = {
            'outing_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }