from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def profile_doctor_view(request):

    doctor = hospital.doctors.get(request.session["doctor_id"])

    return render(request, 'profile_doctor.html', {
        'doctor': doctor
    })