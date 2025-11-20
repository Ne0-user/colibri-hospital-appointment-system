from django.shortcuts import render, redirect
import os

def doctors_managment_view(request):
    return render(request, 'doctors_managment.html')