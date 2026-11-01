from django.urls import path
from . import views

urlpatterns = [
    path('login_member/', views.login_member, name = "login_member"),
    path('patient_signup/', views.patient_signup, name = "patient_signup"),
    path('doctor_signup/', views.doctor_signup, name = "doctor_signup"),
    path('logout_member/', views.logout_member, name = 'logout_member'),
]