from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def search_patient_view(request):
   doctor = hospital.doctors.get(request.session["doctor_id"])
   gender = request.GET.get("gender")
   allergy = request.GET.get("allergy")
   
   return render(request, 'search_patient.html', {
      "doctor": doctor
      })