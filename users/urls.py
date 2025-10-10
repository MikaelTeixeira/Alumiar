from django.urls import path
from . import views

urlpatterns= [
    path("login/", views.login, name="login"),
    path("register/", views.select_register, name="select_register"),
    path("register/student/", views.student_register, name="student_register"),
    path("register/psy/", views.psy_register, name="psy_register"),
    path("register/patient/", views.patient_register, name="patient_register"),
    path("logged/homepage/", views.Homepage, name="homepage"),
]