from django.shortcuts import render, redirect

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

def confirmacao_registro(request):
    return render(request, "users/registered.html")


def psicologo_dashboard(request):
    return render(request, "users/psychologist-dashboard.html")

def psicologo_agenda(request):
    return render(request, "users/psychologist-schedule.html")

def psicologo_anotacoes(request):
    return render(request, "users/psychologist-records.html")

def consultas_marcadas(request):
    return render(request, "users/my-appointments.html")

def historico(request):
    return render(request,"users/history.html")

def reclamacoes(request):
    return render(request,"users/complaints.html")
