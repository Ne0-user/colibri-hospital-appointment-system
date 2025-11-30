from django.shortcuts import render, redirect
from django.contrib import messages
from ..hospital_instance import hospital
from ..Doctors import Doctor 

def register_new_patient_view(request):

    doctor = hospital.doctors.get(request.session["doctor_id"])

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        last_name = request.POST.get("Lname", "").strip()
        age = request.POST.get("age", "").strip()
        password = request.POST.get("password", "")
        comp = request.POST.get("Comp", "")
        gender = request.POST.get("gender", "")
        imageURL = request.POST.get("imageURL", "").strip()
        allergies_list = request.POST.getlist("allergies-list")

        if not all([name, last_name, age, password, comp]):
            messages.error(request, "Rellena todos los campos obligatorios.")
            return redirect("register_new_patient")

        if password != comp:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect("register_new_patient")

        try:
            age = int(age)
        except ValueError:
            messages.error(request, "Edad inválida.")
            return redirect("register_new_patient")
        
        hospital.create_and_assign_patient(name,last_name,age,password,gender,imageURL,allergies_list,doctor.id)


        return redirect("workspace")

    
    return render(request, 'register_new_patient.html', {
        'doctor': doctor
    })
