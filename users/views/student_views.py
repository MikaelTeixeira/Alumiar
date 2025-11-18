from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.db import transaction
from users.models import StudentProfile

User = get_user_model()

@transaction.atomic
def register_student(request):

    field_errors = {
        "nome_completo": [],
        "email": [],
        "password": [],
        "cpf": [],
        "data_nascimento": [],
        "crp_supervisor": [],
        "comprovante_matricula": [],
        "documento_oficial": [],
        "foto_perfil": []
    }

    if request.method == "POST":

        nome = request.POST.get("nome_completo")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpf = request.POST.get("cpf") or None
        birth = request.POST.get("data_nascimento")
        crp_supervisor = request.POST.get("crp_supervisor") or None

        comprovante = request.FILES.get("comprovante_matricula")
        documento = request.FILES.get("documento_oficial")
        foto = request.FILES.get("foto_perfil")

        has_error = False

        if not nome:
            field_errors["nome_completo"].append("O nome completo é obrigatório.")
            has_error = True

        if not email:
            field_errors["email"].append("O e-mail é obrigatório.")
            has_error = True

        if not password:
            field_errors["password"].append("A senha é obrigatória.")
            has_error = True

        if not birth:
            field_errors["data_nascimento"].append("A data de nascimento é obrigatória.")
            has_error = True

        if not comprovante:
            field_errors["comprovante_matricula"].append("O comprovante de matrícula é obrigatório.")
            has_error = True

        if not documento:
            field_errors["documento_oficial"].append("O documento oficial é obrigatório.")
            has_error = True

        if not foto:
            field_errors["foto_perfil"].append("A foto de perfil é obrigatória.")
            has_error = True

        if has_error:
            return render(request, "users/student_register.html", {"field_errors": field_errors})

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                cpf=cpf,
                data_nascimento=birth,
                senha_custom=password,
                user_type="STD"
            )
        except Exception as e:
            field_errors["email"].append("Erro ao criar usuário. Verifique os dados informados.")
            print("ERRO REAL:", e)
            return render(request, "users/student_register.html", {"field_errors": field_errors})

        try:
            StudentProfile.objects.create(
                user=user,
                nome_completo=nome,
                comprovante_matricula=comprovante,
                documento_oficial=documento,
                foto_perfil=foto
            )
        except Exception as e:
            print("ERRO REAL:", e)
            user.delete()
            field_errors["comprovante_matricula"].append("Erro ao criar perfil do estudante.")
            return render(request, "users/student_register.html", {"field_errors": field_errors})

        return redirect("registered")

    return render(request, "users/student_register.html", {"field_errors": field_errors})
