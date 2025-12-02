from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def new_appointment_view(request):
    doctor = hospital.doctors.get(request.session["doctor_id"])

    patient_id = request.GET.get("id")

    if patient_id:
        request.session["current_patient"] = patient_id
    else:
        patient_id = request.session.get("current_patient")

    if not patient_id:
        return redirect("workspace")

    patient = hospital.patients.get(patient_id)

    if request.method == "POST":
       reason = request.POST.get("Reason")
       lab = request.POST.get("Lab Results")
       treatment = request.POST.get("Treatment")
       follow = request.POST.get("Follow-up")

       hospital.add_note_patient(
           patient=patient,
           reason=reason,
           lab=lab,
           treatment=treatment,
           follow=follow
       )

    return render(request, "new_appointment.html", {
        "doctor": doctor,
    })