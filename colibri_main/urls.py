from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('WorkSpace/', views.WorkSpace_view, name='WorkSpace'),
    path('register/', views.register_view, name='register'),
]