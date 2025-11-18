from django import forms
from .models import *
from django.contrib.auth import authenticate



# FORM DO USUÁRIO BASE
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "cpf", "data_nascimento", "senha_custom"]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"}),
            "senha_custom": forms.PasswordInput(attrs={"placeholder": "Digite sua senha"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["senha_custom"])
        return user
    
    def clean_cpf(self):
        raw = self.cleaned_data.get("cpf", "")
        cpf = normaliza_cpf(raw)
        if not cpf:
            raise forms.ValidationError("CPF inválido — digite 11 números (pontos e traços são aceitos).")
        # checar duplicatas (ignora o próprio usuário em update se quiser)
        if CustomUser.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Este CPF já está cadastrado.")
        return cpf



# FORM PACIENTE
class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ["nome_completo", "foto_perfil"]


# FORM ESTUDANTE
from django import forms
from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = [
            "nome_completo",
            "comprovante_matricula",
            "documento_oficial",
            "foto_perfil",
        ]

# FORM PSICÓLOGO
class PsychologistProfileForm(forms.ModelForm):
    class Meta:
        model = PsychologistProfile
        fields = ["nome_completo", "crp", "documento_oficial", "curriculo", "foto_perfil"]



class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail")
    senha_custom = forms.CharField(label="Senha", widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        senha = cleaned_data.get("senha_custom")

        if email and senha:
            user = authenticate(username=email, password=senha)
            print("🧠 authenticate() retornou:", user) 

            if not user:
                raise forms.ValidationError("E-mail ou senha incorretos.")
            
            cleaned_data["user"] = user

        return cleaned_data
