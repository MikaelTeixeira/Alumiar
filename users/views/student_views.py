from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages
from ..forms import CustomUserForm, StudentProfileForm

@transaction.atomic
def register_student(request):

    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        profile_form = StudentProfileForm(request.POST, request.FILES)

        print("USER_FORM ERRORS:", user_form.errors)
        print("PROFILE_FORM ERRORS:", profile_form.errors)

        if user_form.is_valid() and profile_form.is_valid():

            # cria usuário corretamente com senha hash
            user = user_form.save(commit=False)
            user.user_type = "STD"
            user.save()

            # cria perfil
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, "Estudante registrado com sucesso!")
            return redirect("registered")

        else:
            messages.error(request, "Verifique os campos e tente novamente.")

    else:
        user_form = CustomUserForm()
        profile_form = StudentProfileForm()

    return render(request, "users/student_register.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })
