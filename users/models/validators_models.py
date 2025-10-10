from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_cpf(value):
    """Valida CPF segundo o algoritmo oficial (com dígitos verificadores)."""
    cpf = ''.join(filter(str.isdigit, str(value)))

    if len(cpf) != 11:
        raise ValidationError("CPF deve conter 11 dígitos.")

    if cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido.")

    def dv_calculation(cpf_parcial):
        soma = sum(int(d) * i for d, i in zip(cpf_parcial, range(len(cpf_parcial)+1, 1, -1)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    dv1 = dv_calculation(cpf[:9])
    dv2 = dv_calculation(cpf[:9] + dv1)

    if cpf[-2:] != dv1 + dv2:
        raise ValidationError("CPF inválido.")



def validate_name(value):

    if not value.replace(" ", "").isalpha():
        raise ValidationError("O valor inserido é inválido")
    
    if len(value) < 10:
        raise ValidationError("O valor inserido é muito pequeno")
    
    if len(value) > 75:
        raise ValidationError("O valor inserido é muito grande")


def validate_email(value):
    if not (value.endswith("@gmail.com") or value.endswith("@hotmail.com")):

        raise ValidationError("E-mail inválido. Tente @gmail ou @hotmail")


def validate_password(value):
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


def validate_birthday(value):
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
