from django.shortcuts import render, redirect
from django.db import IntegrityError, transaction
from django.contrib import messages
from ..forms import CustomUserForm, PatientProfileForm
from ..models import normaliza_cpf 

def patient_register(request):
    if request.method == "POST":
        print("POST RECEBIDO:", request.POST)
        user_form = CustomUserForm(request.POST)
        profile_form = PatientProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            try:
                with transaction.atomic():
                    user = user_form.save(commit=False)

                    user.user_type = "PAT"
                    user.save()

                    profile = profile_form.save(commit=False)
                    profile.user = user
                    profile.save()

                messages.success(request, "Cadastro realizado com sucesso! Faça login.")
                return redirect("login")

            except IntegrityError:
                messages.error(request, "E-mail ou CPF já cadastrados. Tente outro.")
    else:
        user_form = CustomUserForm()
        profile_form = PatientProfileForm()

    return render(request, "users/patient_register.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })
