from django.shortcuts import render, redirect
import os
from ..Hospital import Hospital
from ..hospital_instance import hospital

def appointments_view(request):
    return render(request, 'appointments.html')