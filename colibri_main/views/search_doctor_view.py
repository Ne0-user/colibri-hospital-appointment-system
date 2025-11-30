from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def search_doctor_view(request):
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

    return render(request, "search_patient.html", {
        "doctor": doctor,
        "patients": patients
    })