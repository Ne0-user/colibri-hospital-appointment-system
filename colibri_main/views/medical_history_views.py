from django.shortcuts import render, redirect
import os

def medical_history_view(request):
    return render(request, 'medical_history.html')