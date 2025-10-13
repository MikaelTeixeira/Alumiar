from django.shortcuts import render, redirect


def login(request):
    return render(request, 'users/login.html')


def select_register(request):
    return render(request, 'users/select_register.html')


def Homepage(request):
    return render(request, 'users/homepage.html')


def Forget_password(request):
    return render(request, 'users/forgot_password.html')

def Configuration(request):
    return render(request, 'users/configuration.html')

def Consulta(request):
    return render(request, "users/consulta.html")