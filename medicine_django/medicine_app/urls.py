from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name = "home"),
    path('patient_interface/', views.patient_interface, name = 'patient_interface'),
    path("search_doctor", views.search_doctor, name="search_doctor"),
]