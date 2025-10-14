from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators_models import (
    normaliza_cpf,
    validate_email,
    validate_cpf,
    validate_birthday,
    validate_password
)

class CustomUser(AbstractUser):
    USER_TYPES = (
        ("PSY", "Psicólogo"),
        ("STD", "Estudante de Psicologia"),
        ("PAT", "Paciente"),
    )

    user_type = models.CharField(max_length=3, choices=USER_TYPES)
    email = models.EmailField(unique=True, validators=[validate_email])
    cpf = models.CharField(max_length=11, unique=True, validators=[validate_cpf])
    data_nascimento = models.DateField(validators=[validate_birthday])
    senha_custom = models.CharField(max_length=10, validators=[validate_password])

    nome_completo = models.CharField(max_length=150, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["cpf", "data_nascimento", "senha_custom", "user_type"]

    def save(self, *args, **kwargs):
        # --- Normaliza CPF ---
        if hasattr(self, "cpf"):
            cpf_normal = normaliza_cpf(self.cpf)
            if cpf_normal:
                self.cpf = cpf_normal

        # --- Gera nome completo ---
        nome = (self.first_name or "").strip()
        sobrenome = (self.last_name or "").strip()
        nome_completo = f"{nome} {sobrenome}".strip()
        if nome_completo and self.nome_completo != nome_completo:
            self.nome_completo = nome_completo

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email} ({self.get_user_type_display()})"
