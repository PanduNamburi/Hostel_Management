from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('complaints/', views.complaint_list, name='complaint_list'),
    path('complaints/submit/', views.submit_complaint, name='submit_complaint'),
    path('complaints/<int:complaint_id>/update/', views.update_complaint_status, name='update_complaint_status'),

]
