from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db import transaction
from users.models import StudentProfile

User = get_user_model()

@transaction.atomic
def register_student(request):
    if request.method == "POST":

        nome = request.POST.get("nome_completo")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpf = request.POST.get("cpf") or None  # opcional
        birth = request.POST.get("data_nascimento")

        crp_supervisor = request.POST.get("crp_supervisor") or None  # opcional

        comprovante = request.FILES.get("comprovante_matricula")
        documento = request.FILES.get("documento_oficial")
        foto = request.FILES.get("foto_perfil")


        if not nome or not email or not password or not birth:
            messages.error(request, "Preencha todos os campos obrigatórios.")
            return redirect("student_register")

        if not comprovante:
            messages.error(request, "Comprovante de matrícula é obrigatório.")
            return redirect("student_register")

        if not documento:
            messages.error(request, "Documento oficial é obrigatório.")
            return redirect("student_register")

        if not foto:
            messages.error(request, "A foto de perfil é obrigatória.")
            return redirect("student_register")


        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                cpf=cpf,
                data_nascimento=birth,
                crp_supervisor=crp_supervisor,
                is_student=True
            )
        except Exception as e:
            messages.error(request, f"Erro ao criar usuário: {e}")
            return redirect("student_register")

        try:
            StudentProfile.objects.create(
                user=user,
                nome_completo=nome,
                comprovante_matricula=comprovante,
                documento_oficial=documento,
                foto_perfil=foto
            )
        except Exception as e:
            user.delete()  
            messages.error(request, f"Erro ao criar perfil: {e}")
            return redirect("student_register")

        return redirect("registered")

    return render(request, "users/student_register.html")
