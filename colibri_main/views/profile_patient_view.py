from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def profile_patient_view(request):
    doctor = hospital.doctors.get(request.session["doctor_id"])

    patient_id = request.GET.get("id")

    if patient_id:
        request.session["current_patient"] = patient_id
    else:
        patient_id = request.session.get("current_patient")

    if not patient_id:
        return redirect("workspace")

    patient = hospital.patients.get(patient_id)

    return render(request, "profile_patient.html", {
        "doctor": doctor,
        "p": patient
    })

