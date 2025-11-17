from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from ..forms import CustomUserForm, PsychologistProfileForm

@transaction.atomic
def register_psychologist(request):
    if request.method == "POST":

        user_form = CustomUserForm(request.POST)
        profile_form = PsychologistProfileForm(request.POST, request.FILES)

        print("USER FORM ERRORS:", user_form.errors)
        print("PROFILE FORM ERRORS:", profile_form.errors)


        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save(commit=False)
            user.user_type = "PSY"
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, "Psicólogo registrado com sucesso!")
            return redirect("registered")

        else:
            messages.error(request, "Verifique os campos e tente novamente.")

    else:
        user_form = CustomUserForm()
        profile_form = PsychologistProfileForm()

    return render(request, "users/psy_register.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })
