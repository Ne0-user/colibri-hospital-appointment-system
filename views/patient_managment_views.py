from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def patient_managment_view(request):

    doctor = hospital.doctors.get(request.session["doctor_id"])
    
    return render(request, 'patient_managment.html', {
        'doctor': doctor
    })

