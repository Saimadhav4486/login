# user_dashboard/views.py
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import PatientSignupForm, DoctorSignupForm
from django.contrib import messages
from .models import CustomUser

def index(request):
    return render(request,'index.html')
def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            login(request, user)
            print("User logged in successfully")
            return redirect('patient_dashboard')
    else:
        form = PatientSignupForm()

    return render(request, 'patient_signup.html', {'form': form})

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True
            user.save()
            login(request, user)
            messages.success(request, 'Doctor account created successfully!')
            return redirect('doctor_dashboard')
    else:
        form = DoctorSignupForm()

    return render(request, 'doctor_signup.html', {'form': form})

def patient_login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(request, username=user, password=password)
        print("Moved to login")

        if user is not None and user.is_patient:
            print("Before login")
            login(request, user)
            print("After login")
            return redirect('patient_dashboard')
        else:
            print("Login failed")
            messages.error(request, 'Invalid credentials for patient login.')

    return render(request, 'patient_login.html')

def doctor_login(request):
    if request.method == 'POST':
        print("Doctor")
        u = request.POST.get('user')
        p = request.POST.get('password')
        
        user = authenticate(request, username=u, password=p)
        print(user)
        if user is not None and user.is_doctor:
            login(request, user)
            return redirect('doctor_dashboard')  # Redirect to doctor dashboard
        else:
            return HttpResponse("SXDCRGBHJMK")

    return render(request, 'doctor_login.html')

def patient_logout(request):
    logout(request)
    return redirect('patient_login')

def doctor_logout(request):
    logout(request)
    return redirect('doctor_login')

def patient_dashboard(request):
    if request.user.is_authenticated and request.user.is_patient:
        patient_details = CustomUser.objects.get(id=request.user.id)
        return render(request, 'patient_dashboard.html', {'patient_details': patient_details})
    else:
        return redirect('patient_login')

def doctor_dashboard(request):
    if request.user.is_authenticated and request.user.is_doctor:
        # Retrieve doctor details using the logged-in user
        doctor_details = CustomUser.objects.get(id=request.user.id)
        return render(request, 'doctor_dashboard.html', {'doctor_details': doctor_details})
    else:
        return redirect('doctor_login')
