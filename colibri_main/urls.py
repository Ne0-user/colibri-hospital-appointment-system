from django.urls import path
from .views import login_views,view_patient_record_filter_view,add_medical_record_view,add_medical_record_filter_view,toggle_doctor_status,medical_history_views,register_views, search_patient_view, workspace_views,patient_managment_views,doctors_managment_views,appointments_view,register_new_patient_view,register_new_doctor_view,profile_doctor_views,notification_view,deleate_doctor_views,profile_patient_view,search_doctor_view,deleate_patients_views,toggle_patient_status,profile_other_doctor_view

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
    path('profile_other_doctor/', profile_other_doctor_view.profile_other_doctor_view, name='profile_other_doctor'),
    path('notifications/', notification_view.notifications_view, name='notifications'),
    path('profile_patients/', profile_patient_view.profile_patient_view, name='profile_patients'),
    path('search_doctor/', search_doctor_view.search_doctor_view, name='search_doctor'),
    path('deleate_patients/', deleate_patients_views.deleate_patient_view, name='deleate_patients'),
    path('toggle_patient_status/', toggle_patient_status.toggle_patient_status, name='toggle_patient_status'),
    path('deleate_doctor/', deleate_doctor_views.deleate_doctor_view, name='deleate_doctor'),
    path('toggle_doctor_status/', toggle_doctor_status.toggle_doctor_status, name='toggle_doctor_status'),
    path('toggle_doctor_status/', toggle_doctor_status.toggle_doctor_status, name='toggle_doctor_status'),
    path('add_medical_record_filter/', add_medical_record_filter_view.add_medical_record_filter_view, name='add_medical_record_filter'),
    path('add_medical_record/',add_medical_record_view.add_medical_record_view, name='add_medical_record'),
    path('view_patient_record_filter/',view_patient_record_filter_view.view_patient_record_filter_view, name='view_patient_record_filter'),
]