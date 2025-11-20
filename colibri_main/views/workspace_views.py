from django.shortcuts import render, redirect
import os

def workspace_view(request):
    return render(request, "workspace.html")