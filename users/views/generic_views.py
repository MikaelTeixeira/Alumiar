from django.shortcuts import render, redirect


def login(request):
    return render(request, 'users/login.html')


def select_register(request):
    return render(request, 'users/select_register.html')


def Homepage(request):
    return render(request, 'users/homepage.html')


def Forget_password(request):
    return render(request, 'users/forget_password.html')