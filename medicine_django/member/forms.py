# members/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from medicine_app.models import Patient, Doctor

class PatientSignupForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = ('patient_name', 'phone_no', 'age', 'gender', 'DOB', 'blood_group')

class DoctorSignupForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = ('doctor_name', 'phone_no', 'speciality', 'hospital')
