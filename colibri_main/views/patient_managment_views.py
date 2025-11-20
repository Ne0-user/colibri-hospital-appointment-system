from django.shortcuts import render, redirect
import os

def patient_managment_view(request):
    return render(request, 'patient_managment.html')
