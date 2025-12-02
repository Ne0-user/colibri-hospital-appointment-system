from django.shortcuts import render, redirect
from django.contrib import messages
from ..Hospital import Hospital
from ..hospital_instance import hospital

def register_new_doctor_view(request):

    doctor = hospital.doctors.get(request.session["doctor_id"])

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        last_name = request.POST.get("Lname", "").strip()
        age = request.POST.get("age", "").strip()
        password = request.POST.get("password", "")
        comp = request.POST.get("Comp", "")
        gender = request.POST.get("gender", "")
        spec = request.POST.get("speciality", "")
        rank = request.POST.get("rank", "")
        imageURL = request.POST.get("imageURL", "").strip()

        if not all([name, last_name, age, password, comp]):
            messages.error(request, "Rellena todos los campos obligatorios.")
            return redirect("register_new_doctor")
        
        if password != comp:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect("register_new_doctor")
        

        try:
            age = int(age)
        except ValueError:
            messages.error(request, "Edad inválida.")
            return redirect("register_new_doctor")
        
        hospital.create_doctor(name,last_name,age,password,gender,imageURL,spec,rank)

        return redirect("workspace")

    return render(request, 'register_new_doctor.html', {
        'doctor': doctor
    })