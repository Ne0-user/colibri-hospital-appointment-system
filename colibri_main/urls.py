from django.urls import path
from .views import login_views, medical_history_views,register_views, search_patient_view, workspace_views,patient_managment_views,doctors_managment_views,appointments_view,register_new_patient_view,register_new_doctor_view,profile_doctor_views

urlpatterns = [
    path('',login_views.login_view, name='login'),
    path('workspace/', workspace_views.workspace_view, name='workspace'),
    path('register/', register_views.register_view, name='register'),
    path('patient_managment/', patient_managment_views.patient_managment_view, name='patient_managment'),
    path('doctors_managment/', doctors_managment_views.doctors_managment_view, name='doctors_managment'),
    path('medical_history/', medical_history_views.medical_history_view, name='medical_history'),
    path('appointments/', appointments_view.appointments_view, name='appointments'),
    path('register_new_patient/', register_new_patient_view.register_new_patient_view, name='register_new_patient'),
    path('register_new_doctor/', register_new_doctor_view.register_new_doctor_view, name='register_new_doctor'),
    path('search_patient/', search_patient_view.search_patient_view, name='search_patient'),
    path('profile_doctor/', profile_doctor_views.profile_doctor_view, name='profile_doctor'),
]