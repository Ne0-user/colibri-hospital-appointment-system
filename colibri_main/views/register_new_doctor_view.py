from django.shortcuts import render, redirect
import os

def register_new_doctor_view(request):
    return render(request, 'register_new_doctor.html')