from django.shortcuts import render, redirect
from .forms import CustomUserForm, StudentProfileForm, PsychologistProfileForm, PatientProfileForm


def login(request):
    return render(request, 'users/login.html')

def student_register(request):
    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        profile_form = StudentProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
        else:
            user_form = CustomUserForm()
            profile_form = StudentProfileForm()

    return render(request, 'users/student_register.html',{
        "user_form": user_form,
        "profile_form": profile_form
    })

def psy_register(request):
    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        profile_form = PsychologistProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
        else:
            user_form = CustomUserForm()
            profile_form = PsychologistProfileForm()

    return render(request, 'users/psy_register.html',{
        "user_form": user_form,
        "profile_form": profile_form
    })

def patient_register(request):
    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        profile_form = PatientProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
        else:
            user_form = CustomUserForm()
            profile_form = PatientProfileForm()

    return render(request, 'users/patient_register.html',{
        "user_form": user_form,
        "profile_form": profile_form
    })

def Select_register(request):
    return render(request,'users/select_register.html')