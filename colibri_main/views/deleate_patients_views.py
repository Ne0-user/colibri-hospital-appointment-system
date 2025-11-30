from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def deleate_patient_view(request):
    doctor = hospital.doctors.get(request.session["doctor_id"])
    patients = []

    gender = request.POST.get("gender")
    allergy = request.POST.get("allergie")
    only_doctor = request.POST.get("Od")
    search_id = request.POST.get("id")
    if only_doctor == "True":
        only_doctor = True
    elif only_doctor == "False":
        only_doctor = False

    patients = hospital.filter_patients(
        doctor=doctor,
        gender=gender,
        allergies=[allergy] if allergy else None,
        only_doctor=only_doctor,
        fid=search_id
    )

    if request.method == "POST" and "patient_id" in request.POST:
        patient_id = request.POST.get("patient_id")
        patient = hospital.patients.get(patient_id)
        patient.change_status()
        hospital.save_patients()

    if request.method == "POST":
        gender = request.POST.get("gender")
        allergy = request.POST.get("allergie")
        only_doctor = request.POST.get("Od")
        search_id = request.POST.get("id")

        if only_doctor == "True":
            only_doctor = True
        elif only_doctor == "False":
            only_doctor = False

        patients = hospital.filter_patients(
            doctor=doctor,
            gender=gender,
            allergies=[allergy] if allergy else None,
            only_doctor=only_doctor,
            fid=search_id
        )

    return render(request, "deleate_patient.html", {
        "doctor": doctor,
        "patients": patients
    })