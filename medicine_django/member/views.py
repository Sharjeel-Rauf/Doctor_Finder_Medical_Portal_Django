from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import PatientSignupForm, DoctorSignupForm

def login_member(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('patient_interface')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login_member')

    return render(request, 'member/login.html', {})


def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, ("Registration is Successful"))
            return redirect('patient_interface')
    else:
        form = PatientSignupForm()

    return render(request, 'member/patient_signup.html', {'form': form})



def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, ("Registration is Successful"))
            # Doctors land on the doctor list, where their new profile now appears
            return redirect('patient_interface')
    else:
        form = DoctorSignupForm()

    return render(request, 'member/doctor_signup.html', {'form': form})

def logout_member(request):
    logout(request)
    return redirect('home')