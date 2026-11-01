from django.shortcuts import render
from .models import Patient, Doctor
from django.db.models import Q

# Create your views here.
def home_view(request):
    return render(request, 'medicine_app/home.html', {})

def patient_interface(request):
    doctor_list = Doctor.objects.all()
    return render(request, 'medicine_app/patient_interface.html', {'doctor_list': doctor_list})

# search doctor
def search_doctor(request):
    if request.method == "POST":
        searched = request.POST['searched']
        doctors = Doctor.objects.filter(
            Q(doctor_name__icontains=searched) |  # Search in name
            Q(speciality__icontains=searched) |   # Search in speciality
            Q(hospital__icontains=searched)       # Search in hospital
            )
        return render(request, "medicine_app/search.html", {'searched': searched, 'doctors': doctors})
    else:
        return render(request, "medicine_app/search.html", {})
