from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital


def login_view(request):
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")

        doctor= hospital.login_doctors(user,password)

        if doctor:
            request.session["doctor_id"]=doctor.id
            return redirect("workspace")
        


    return render(request, "login.html",
        {"error": "Usuario no encontrado"}) 
    
