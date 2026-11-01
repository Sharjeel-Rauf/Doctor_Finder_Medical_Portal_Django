from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128, default='')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

class Patient(models.Model):
    patient_id = models.IntegerField(null=True, blank=True)
    patient_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    age = models.IntegerField(null=True, blank=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(choices=gender_choices, max_length=10, default='other')
    DOB = models.DateTimeField(null=True, blank=True)
    blood_group_choices = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('Unknown', 'Unknown'),
    ]
    blood_group = models.CharField(max_length=10, choices=blood_group_choices, default='Unknown')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        return self.patient_name

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    speciality = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.doctor_name
