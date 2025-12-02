from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def doctors_managment_view(request):
    doctor = hospital.doctors.get(request.session["doctor_id"])

    return render(request, 'doctors_managment.html', {
        'doctor': doctor
    })