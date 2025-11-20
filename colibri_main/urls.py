from django.urls import path
from .views import login_views, medical_history_views,register_views, workspace_views,patient_managment_views,doctors_managment_views

urlpatterns = [
    path('',login_views.login_view, name='login'),
    path('workspace/', workspace_views.workspace_view, name='workspace'),
    path('register/', register_views.register_view, name='register'),
    path('patient_managment/', patient_managment_views.patient_managment_view, name='patient_managment'),
    path('doctors_managment/', doctors_managment_views.doctors_managment_view, name='doctors_managment'),
    path('medical_history/', medical_history_views.medical_history_view, name='medical_history'),
]