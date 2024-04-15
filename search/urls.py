# urls.py
from django.urls import path
from . import views

app_name = "search"

urlpatterns = [
    path('find/', views.find, name='find'),


    # Add similar URLs for signup, logout, etc.
]
