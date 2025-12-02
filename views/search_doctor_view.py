from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def search_doctor_view(request):
    doctor = hospital.doctors.get(request.session["doctor_id"])
    patients = []

    gender = request.POST.get("gender")
    rank = request.POST.get("rank")
    speciality = request.POST.get("speciality")
    search_id = request.POST.get("id")

    doctors=hospital.filter_doctors(
        fid=search_id,
        gender=gender,
        rank=rank,
        speciality=speciality
        )
  

    if request.method == "POST":
        gender = request.POST.get("gender")
        rank = request.POST.get("rank")
        speciality = request.POST.get("speciality")
        search_id = request.POST.get("id")

        doctors=hospital.filter_doctors(
            fid=search_id,
            gender=gender,
            rank=rank,
            speciality=speciality
        )


        
    return render(request, "search_doctor.html", {
        "doctor": doctor,
        "doctors": doctors
    })