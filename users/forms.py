from django import forms
from django.contrib.auth import authenticate
from .models import CustomUser, PatientProfile, StudentProfile, PsychologistProfile
from .models.validators_models import normaliza_cpf


# FORM DO USUÁRIO BASE — CADASTRO
class CustomUserForm(forms.ModelForm):
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"placeholder": "Digite sua senha"})
    )

    class Meta:
        model = CustomUser
        fields = ["email", "cpf", "data_nascimento"]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        password = self.cleaned_data["password"]
        user.set_password(password)

        if commit:
            user.save()
        return user
    
    def clean_cpf(self):
        raw = self.cleaned_data.get("cpf", "")
        cpf = normaliza_cpf(raw)

        if not cpf:
            raise forms.ValidationError("CPF inválido — digite 11 números (pontos e traços são aceitos).")

        if CustomUser.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Este CPF já está cadastrado.")

        return cpf



class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ["nome_completo", "foto_perfil"]


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = [
            "nome_completo",
            "comprovante_matricula",
            "documento_oficial",
            "foto_perfil",
        ]


class PsychologistProfileForm(forms.ModelForm):
    class Meta:
        model = PsychologistProfile
        fields = ["nome_completo", "crp", "documento_oficial", "curriculo", "foto_perfil"]



class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        senha = cleaned_data.get("password")

        if email and senha:
            user = authenticate(username=email, password=senha)
            print("authenticate() retornou:", user)

            if not user:
                raise forms.ValidationError("E-mail ou senha incorretos.")

            cleaned_data["user"] = user

        return cleaned_data
