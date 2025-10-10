from django.shortcuts import render, redirect
from ..forms import (
    CustomUserForm,
    PatientProfileForm
)

def patient_register(request):
    user_form = CustomUserForm()
    profile_form = PatientProfileForm()

    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        profile_form = PatientProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')

    return render(request, 'users/patient_register.html', {
        "user_form": user_form,
        "profile_form": profile_form
    })