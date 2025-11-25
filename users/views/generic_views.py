from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib import messages
from users.models import CustomUser


def select_register(request):
    return render(request, 'users/select_register.html')


def Homepage(request):
    return render(request, 'users/homepage.html')


def Forget_password(request):
    return render(request, 'users/forgot_password.html')

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

@login_required
def configuracoes(request):
    user = request.user

    if request.method == "POST":
        email = request.POST.get("email")          
        senha = request.POST.get("password")   

        alterou_algo = False

        if email and email.strip():
            user.email = email
            alterou_algo = True

        if senha and senha.strip():
            user.set_password(senha)
            alterou_algo = True

        if alterou_algo:
            user.save()

            messages.success(request, "Alterações salvas com sucesso!")

            if senha:
                update_session_auth_hash(request, user)
        
        
        if email and email.strip() and email != user.email:

            if CustomUser.objects.exclude(pk=user.pk).filter(email=email).exists():
                messages.error(request, "Este e-mail já está em uso.")
                return redirect("configuracoes")

            user.email = email

            alterou_algo = True

        if senha and senha.strip():
            user.set_password(senha)

            user.password = senha

            alterou_algo = True
        return redirect("configuracoes")

    return render(request, "users/configuration.html")


@login_required
def delete_account(request):
    user = request.user

    logout(request)

    user.delete()
    return redirect("login")