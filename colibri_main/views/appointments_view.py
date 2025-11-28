from django.shortcuts import render, redirect
import os

def appointments_view(request):
    return render(request, 'appointments.html')