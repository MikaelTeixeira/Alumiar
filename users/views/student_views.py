from django.shortcuts import render, redirect
from ..forms import (
    CustomUserForm,
    StudentProfileForm,
)

def student_register(request):
    user_form = CustomUserForm()
    profile_form = StudentProfileForm()

    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        profile_form = StudentProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return render(request, 'users/register_confirmation.html')

    return render(request, 'users/student_register.html', {
        "user_form": user_form,
        "profile_form": profile_form
    })
