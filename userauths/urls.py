# urls.py
from django.urls import path
from . import views

app_name = "userauths"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.signup_view, name='register'),
    path('logout/', views.login_view, name="logout"),

    # Add similar URLs for signup, logout, etc.
]
