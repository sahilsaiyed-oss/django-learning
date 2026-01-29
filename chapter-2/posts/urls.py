from django.urls import path
from . import views

urlpatterns = [
    # Add the 's' at the end to match your views.py
    path('', views.posts_lists) 
]