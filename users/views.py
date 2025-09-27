from django.shortcuts import render

def generic_login(request):
    return render(request, 'users/generic_login.html')

def student_register(request):
    return render(request, 'users/student_register.html')

def psy_register(request):
    return render(request, 'users/psy_register.html')

def pacient_register(request):
    return render(request, 'users/patient_register.html')