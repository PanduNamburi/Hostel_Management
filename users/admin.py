from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    def has_module_permission(self, request):
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'warden'

    def has_view_permission(self, request, obj=None):
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'warden'

admin.site.register(CustomUser, CustomUserAdmin)
