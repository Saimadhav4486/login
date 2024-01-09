# user_dashboard/urls.py
from django.urls import path
from .views import patient_signup, doctor_signup, patient_login, doctor_login, patient_logout, doctor_logout, patient_dashboard, doctor_dashboard, index

urlpatterns = [
    path('',index,name='default'),
    path('patient_signup', patient_signup, name='patient_signup'),
    path('doctor_signup', doctor_signup, name='doctor_signup'),
    path('patient_login', patient_login, name='patient_login'),
    path('doctor_login', doctor_login, name='doctor_login'),
    path('patient_logout', patient_logout, name='patient_logout'),
    path('doctor_logout', doctor_logout, name='doctor_logout'),
    path('patient_dashboard', patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard', doctor_dashboard, name='doctor_dashboard'),
]
