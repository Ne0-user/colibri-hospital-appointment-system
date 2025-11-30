from django.shortcuts import redirect
from ..Hospital import Hospital
from ..hospital_instance import hospital
from ..Patients import Patients

def toggle_patient_status(request):
    if request.method == "POST":
        patient_id = request.POST.get("patient_id")
        patient = hospital.patients.get(patient_id)
        if patient:
            patient.change_status()
            hospital.save_patients()
       
        return redirect('deleate_patients')

