from django.shortcuts import render, redirect
from ..hospital_instance import hospital
from ..Note import Note

def view_patient_record_view(request):
    doctor = hospital.doctors.get(request.session["doctor_id"])

    patient_id = request.GET.get("id")

    if patient_id:
        request.session["current_patient"] = patient_id
    else:
        patient_id = request.session.get("current_patient")

    if not patient_id:
        return redirect("workspace")

    patient = hospital.patients.get(patient_id)

    notes = patient.get_all_notes()

    return render(request, "view_patient_record.html", {
        "doctor": doctor,
        "patient": patient,
        "notes": notes
    })

