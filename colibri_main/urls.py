from django.urls import path
from .views import login_views,register_views, workspace_views

urlpatterns = [
    path('',login_views.login_view, name='login'),
    path('workspace/', workspace_views.workspace_view, name='workspace'),
    path('register/', register_views.register_view, name='register'),
]