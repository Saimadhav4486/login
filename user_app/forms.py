# user_dashboard/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class PatientSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'profile_picture', 'address_line1', 'city', 'state', 'pincode']

class DoctorSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'profile_picture', 'address_line1', 'city', 'state', 'pincode']
