from django.shortcuts import render, redirect
import os

def register_new_patient_view(request):
    return render(request, 'register_new_patient.html')