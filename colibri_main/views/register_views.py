from django.shortcuts import render, redirect
import os

def register_view(request):
   return render(request, 'register.html')