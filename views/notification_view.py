from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital


def notifications_view(request):
    doctor = hospital.doctors.get(request.session["doctor_id"])

    notis = hospital.notifications.get_notifications()

    return render(request, "notifications.html", {
        "doctor": doctor,
        "notifications": notis
    })
