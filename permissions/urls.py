from django.urls import path
from .views import request_permission, outing_permission, return_notification
from .views import track_status

urlpatterns = [
    path('request/', request_permission, name='request_permission'),
    path('outing/<int:permission_id>/', outing_permission, name='outing_permission'),
    path('return/<int:permission_id>/', return_notification, name='return_notification'),
    path('track/', track_status, name='track_status'),
]