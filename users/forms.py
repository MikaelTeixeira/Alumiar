from django import forms
from .models import CustomUser, PsychologistProfile, StudentProfile, PatientProfile

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["user_type", "email", "cpf", "data_nascimento", "senha_custom"]

class PsychologistProfileForm(forms.ModelForm):
    class Meta:
        model = PsychologistProfile
        fields = ["nome_completo", "crp", "documento_oficial", "curriculo", "foto_perfil"]

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ["nome_completo", "comprovante_matricula", "documento_oficial", "foto_perfil"]

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ["nome_completo", "foto_perfil"]
