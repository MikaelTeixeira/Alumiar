from django.shortcuts import render, redirect
from django.db import IntegrityError, transaction
from django.contrib import messages
from ..forms import CustomUserForm, PatientProfileForm
from ..models import normaliza_cpf  # importante

def patient_register(request):
    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        profile_form = PatientProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            try:
                with transaction.atomic():
                    user = user_form.save(commit=False)

                    # Normaliza o CPF antes de salvar
                    user.cpf = normaliza_cpf(user_form.cleaned_data.get("cpf", ""))

                    # Define o tipo de usuário
                    user.user_type = "PAT"

                    # Define a senha
                    user.set_password(user_form.cleaned_data.get("senha_custom"))

                    user.save()

                    profile = profile_form.save(commit=False)
                    profile.user = user
                    profile.save()

                messages.success(request, "Cadastro realizado com sucesso! Faça login.")
                return redirect("login")

            except IntegrityError:
                messages.error(request, "E-mail ou CPF já cadastrados. Tente outro.")
        else:
            messages.error(request, "Verifique os campos e tente novamente.")
    else:
        user_form = CustomUserForm()
        profile_form = PatientProfileForm()

    return render(request, "users/patient_register.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })
