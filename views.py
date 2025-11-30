from django.shortcuts import render, redirect
import os

def login_view(request):
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        txt_path = os.path.join(base_dir, "data", "prueba.txt")

        with open(txt_path, "r", encoding="utf-8") as f:
            for linea in f:
                u, p = linea.strip().split(",")
                if user == u and password == p:
                    return redirect("WorkSpace")

        return render(request, "login.html", {"error": "Credenciales incorrectas"})

    return render(request, "login.html")


def WorkSpace_view(request):
    return render(request, "WorkSpace.html")


def register_view(request):
   return render(request, 'register.html')
