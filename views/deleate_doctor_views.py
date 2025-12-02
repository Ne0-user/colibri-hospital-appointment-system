from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def deleate_doctor_view(request):
    doctor = hospital.doctors.get(request.session["doctor_id"])

    doctors = []

    if request.method == "POST":

        if "patient_id" in request.POST:
            doc_id = request.POST.get("patient_id")
            doc = hospital.doctors.get(doc_id)

        gender = request.POST.get("gender")
        rank = request.POST.get("rank")
        speciality = request.POST.get("speciality")
        search_id = request.POST.get("id")


        doctors = hospital.filter_doctors(
            fid=search_id,
            gender=gender,
            rank=rank,
            speciality=speciality,
        )

    return render(request, "deleate_doctor.html", {
        "doctor": doctor,
        "doctors": doctors
    })
