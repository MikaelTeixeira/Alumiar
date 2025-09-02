from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
import re


# =========================================================== #
#                        VALIDADORES                          #
# =========================================================== #


def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, str(cpf)))
    
    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    def calcular_dv(cpf_parcial):
        soma = sum(int(d) * i for d, i in zip(cpf_parcial, range(len(cpf_parcial)+1, 1, -1)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    dv1 = calcular_dv(cpf[:9])
    dv2 = calcular_dv(cpf[:9] + dv1)

    return cpf[-2:] == dv1 + dv2



def validate_nome(value):

    if not value.replace(" ", "").isalpha():
        raise ValidationError("O valor inserido é inválido")
    if len(value) < 10:
        raise ValidationError("O valor inserido é muito pequeno")
    if len(value) > 75:
        raise ValidationError("O valor inserido é muito grande")


def validate_email(value):
    if not (value.endswith("@gmail.com") or value.endswith("@hotmail.com")):
        raise ValidationError("E-mail inválido. Tente @gmail ou @hotmail")


def validate_senha(value):
    if len(value) < 5:
        raise ValidationError("Senha muito curta")
    if len(value) > 10:
        raise ValidationError("Senha muito longa")
    if not re.match(r"^[a-zA-Z0-9]+$", value):
        raise ValidationError("A senha deve ser alfanumérica")


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError("CPF inválido")
    if len(value) != 11:
        raise ValidationError("Tamanho inválido")
    if value == "00000000000":
        raise ValidationError("CPF inválido")


def validate_data_nascimento(value):
    if len(str(value)) != 10:
        raise ValidationError("Data de nascimento inválida")


def validate_file_size(value):
    """Máx 5MB"""
    filesize = value.size
    if filesize > 5 * 1024 * 1024:
        raise ValidationError("Documento maior que o permitido (5MB)")


def validate_pdf(value):
    if not value.name.lower().endswith(".pdf"):
        raise ValidationError("Formato inválido, apenas PDF permitido")


def validate_image_or_pdf(value):
    valid_ext = (".jpg", ".jpeg", ".pdf")
    if not value.name.lower().endswith(valid_ext):
        raise ValidationError("Formato inválido, tente PDF, JPEG ou JPG")


# =========================================================== #
#                   MODELO BASE DE USUÁRIO                    #
# =========================================================== #

class CustomUser(AbstractUser):
    USER_TYPES = (
        ("PSY", "Psicólogo"),
        ("STD", "Estudante de Psicologia"),
        ("PAT", "Paciente"),
    )

    user_type = models.CharField(max_length=3, choices=USER_TYPES)
    email = models.EmailField(unique=True, validators=[validate_email])
    cpf = models.CharField(max_length=11, unique=True, validators=[validate_cpf])
    data_nascimento = models.DateField(validators=[validate_data_nascimento])
    senha_custom = models.CharField(max_length=10, validators=[validate_senha])

    REQUIRED_FIELDS = ["email", "cpf", "data_nascimento", "senha_custom"]

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"


# =========================================================== #
#                        PSICÓLOGO                            #
# =========================================================== #

class PsychologistProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=75, validators=[validate_nome])
    crp = models.CharField(max_length=8)

    documento_oficial = models.FileField(
        upload_to="documentos/",
        validators=[validate_image_or_pdf, validate_file_size]
    )
    curriculo = models.FileField(
        upload_to="curriculos/",
        validators=[validate_pdf, validate_file_size],
        blank=True, null=True
    )
    foto_perfil = models.FileField(
        upload_to="fotos_perfil/",
        validators=[validate_image_or_pdf, validate_file_size]
    )

    def __str__(self):
        return f"Psicólogo: {self.nome_completo}"


# =========================================================== #
#                        ESTUDANTE                            #
# =========================================================== #

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=75, validators=[validate_nome])

    comprovante_matricula = models.FileField(
        upload_to="matriculas/",
        validators=[validate_image_or_pdf, validate_file_size]
    )
    documento_oficial = models.FileField(
        upload_to="documentos/",
        validators=[validate_image_or_pdf, validate_file_size]
    )
    foto_perfil = models.FileField(
        upload_to="fotos_perfil/",
        validators=[validate_image_or_pdf, validate_file_size]
    )

    def __str__(self):
        return f"Estudante: {self.nome_completo}"


# =========================================================== #
#                        PACIENTE                             #
# =========================================================== #

class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=75, validators=[validate_nome])

    foto_perfil = models.FileField(
        upload_to="fotos_perfil/",
        validators=[validate_image_or_pdf, validate_file_size]
    )

    def __str__(self):
        return f"Paciente: {self.nome_completo}"
