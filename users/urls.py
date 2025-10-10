from django.urls import path
from . import views

urlpatterns= [
    path("login/", views.login, name="login"),
    path("register/", views.Select_register, name="Select_register"),
    path("register/student/", views.student_register, name="student_register"),
    path("register/psy/", views.psy_register, name="psy_register"),
    path("register/patient/", views.patient_register, name="patient_register"),
]