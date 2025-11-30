from django.shortcuts import redirect
from ..Hospital import Hospital
from ..hospital_instance import hospital
from ..Patients import Patients

def toggle_doctor_status(request):
    if request.method == "POST":
        patient_id = request.POST.get("patient_id")
        patient = hospital.doctors.get(patient_id)
        if patient:
            hospital.deleate_doctor(patient)
            hospital.save_patients()
       
        return redirect('deleate_doctor')