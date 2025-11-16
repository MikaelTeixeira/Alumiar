# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db import transaction
from ..models import PsychologistProfile

User = get_user_model()

@transaction.atomic
def register_psychologist(request):
    if request.method == "POST":

        nome = request.POST.get("nome_completo")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpf = request.POST.get("cpf")
        birth = request.POST.get("data_nascimento")
        crp = request.POST.get("crp")

        documento = request.FILES.get("documento_oficial")
        curriculo = request.FILES.get("curriculo")   
        foto = request.FILES.get("foto_perfil")

        if not nome or not email or not password or not cpf or not birth or not crp:
            messages.error(request, "Preencha todos os campos obrigatórios.")
            return redirect("psy_register")

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                cpf=cpf,
                data_nascimento=birth,
                password=password,
                is_psychologist=True  
            )
        except Exception as e:
            messages.error(request, "Erro ao criar usuário: " + str(e))
            return redirect("psy_register")

        try:
            PsychologistProfile.objects.create(
                user=user,
                nome_completo=nome,
                crp=crp,
                documento_oficial=documento,
                curriculo=curriculo,
                foto_perfil=foto
            )
        except Exception as e:
            messages.error(request, "Erro ao criar perfil: " + str(e))
            user.delete()
            return redirect("psy_register")

        return redirect("registered")

    return render(request, "users/psy_register.html")
