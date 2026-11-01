# members/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from medicine_app.models import User, Patient, Doctor

# Creates the login account and the matching patient or doctor profile in one form
class SignupForm(UserCreationForm):
    profile_model = None
    profile_fields = ()
    profile_widgets = {}
    role = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add the profile fields (name, phone number, ...) after the account fields
        self.fields.update(forms.fields_for_model(
            self.profile_model, fields=self.profile_fields, widgets=self.profile_widgets))

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        setattr(user, self.role, True)
        user.save()
        profile_data = {field: self.cleaned_data[field] for field in self.profile_fields}
        self.profile_model.objects.create(user=user, **profile_data)
        return user

class PatientSignupForm(SignupForm):
    profile_model = Patient
    profile_fields = ('patient_name', 'phone_no', 'age', 'gender', 'DOB', 'blood_group')
    profile_widgets = {'DOB': forms.DateInput(attrs={'type': 'date'})}
    role = 'is_patient'

class DoctorSignupForm(SignupForm):
    profile_model = Doctor
    profile_fields = ('doctor_name', 'phone_no', 'speciality', 'hospital')
    role = 'is_doctor'
