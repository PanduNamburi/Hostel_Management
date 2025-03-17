from django.urls import path
from .views import complaint_list, submit_complaint, update_complaint_status

urlpatterns = [
    path("", complaint_list, name="complaint_list"),
    path("submit/", submit_complaint, name="submit_complaint"),
    path("update/<int:complaint_id>/", update_complaint_status, name="update_complaint_status"),
]
