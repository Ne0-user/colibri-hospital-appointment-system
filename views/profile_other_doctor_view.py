from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def profile_other_doctor_view(request):
    doctor = hospital.doctors.get(request.session["doctor_id"])
    d2_id = request.GET.get("id")

    if d2_id:
        request.session["current_patient"] = d2_id
    else:
        d2_id = request.session.get("current_patient")

    if not d2_id:
        return redirect("workspace")

    d2 = hospital.doctors.get(d2_id)

    return render(request, 'profile_other_doctor.html', {
        'doctor': doctor,
        'd2': d2
        
    })