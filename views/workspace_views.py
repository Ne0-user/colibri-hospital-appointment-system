from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def workspace_view(request):
    if "doctor_id" not in request.session:
        return redirect("login")
    
    doctor = hospital.doctors.get(request.session["doctor_id"])
    
    return render(request, "workspace.html", {"doctor": doctor})
