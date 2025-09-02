from django.urls import path
from . import views

urlpatterns= [
    path("login/", views.generic_login, name="generic_login"),
    path("register/student/", views.student_register, name="student_register"),
    path("register/psy/", views.psy_register, name="psy_register"),
    path("register/pacient/", views.pacient_register, name="pacient_register"),
]