from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def medical_history_view(request):
    doctor = hospital.doctors.get(request.session["doctor_id"])

    
    return render(request, 'medical_history.html', {
        'doctor': doctor
    })