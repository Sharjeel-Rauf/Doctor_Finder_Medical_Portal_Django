from django.test import TestCase
from django.urls import reverse
from medicine_app.models import User, Patient, Doctor

PASSWORD = 'Str0ng-pass-123'

PATIENT_DATA = {
    'username': 'ali', 'email': 'ali@example.com',
    'password1': PASSWORD, 'password2': PASSWORD,
    'patient_name': 'Ali Khan', 'phone_no': '03001234567', 'age': 30,
    'gender': 'M', 'DOB': '1994-05-01', 'blood_group': 'B+',
}

DOCTOR_DATA = {
    'username': 'drsara', 'email': 'sara@example.com',
    'password1': PASSWORD, 'password2': PASSWORD,
    'doctor_name': 'Dr Sara Ahmed', 'phone_no': '03111234567',
    'speciality': 'Cardiology', 'hospital': 'City Hospital',
}

class SignupTests(TestCase):

    def test_signup_pages_load(self):
        for url_name in ('patient_signup', 'doctor_signup', 'login_member'):
            self.assertEqual(self.client.get(reverse(url_name)).status_code, 200)

    def test_patient_signup_creates_account_and_profile(self):
        response = self.client.post(reverse('patient_signup'), PATIENT_DATA)

        self.assertRedirects(response, reverse('patient_interface'))
        user = User.objects.get(username='ali')
        self.assertTrue(user.is_patient)
        self.assertFalse(user.is_doctor)
        self.assertTrue(user.check_password(PASSWORD))
        self.assertEqual(user.patient_profile.patient_name, 'Ali Khan')
        self.assertEqual(user.patient_profile.blood_group, 'B+')
        # The new patient is logged in straight away
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)

    def test_doctor_signup_creates_account_and_profile(self):
        response = self.client.post(reverse('doctor_signup'), DOCTOR_DATA)

        self.assertRedirects(response, reverse('patient_interface'))
        user = User.objects.get(username='drsara')
        self.assertTrue(user.is_doctor)
        self.assertFalse(user.is_patient)
        self.assertEqual(user.doctor.speciality, 'Cardiology')
        # The new doctor shows up in the doctor list with their email
        response = self.client.get(reverse('patient_interface'))
        self.assertContains(response, 'Dr Sara Ahmed')
        self.assertContains(response, 'sara@example.com')

    def test_new_account_can_log_in(self):
        self.client.post(reverse('doctor_signup'), DOCTOR_DATA)
        self.client.get(reverse('logout_member'))

        response = self.client.post(reverse('login_member'), {'username': 'drsara', 'password': PASSWORD})
        self.assertRedirects(response, reverse('patient_interface'))

    def test_duplicate_email_is_rejected(self):
        User.objects.create_user(username='someone', email='ali@example.com', password=PASSWORD)

        response = self.client.post(reverse('patient_signup'), PATIENT_DATA)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There was an error with the form')
        self.assertFalse(User.objects.filter(username='ali').exists())
        self.assertFalse(Patient.objects.exists())

    def test_mismatched_passwords_create_nothing(self):
        response = self.client.post(reverse('doctor_signup'), {**DOCTOR_DATA, 'password2': 'Different-pass-456'})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.exists())
        self.assertFalse(Doctor.objects.exists())
