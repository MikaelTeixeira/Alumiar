from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators_models import normaliza_cpf
from .validators_models import validate_email, validate_cpf, validate_birthday, validate_password

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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["cpf", "data_nascimento", "senha_custom", "user_type"]

    def save(self, *args, **kwargs):
        if hasattr(self, "cpf"):
            cpf_normal = normaliza_cpf(self.cpf)
            if cpf_normal:
                self.cpf = cpf_normal
            else:
                # Se preferir lançar erro ao salvar
                # raise ValueError("CPF inválido: deve ter 11 dígitos numéricos.")
                self.cpf = self.cpf  # ou deixar como está para que validação de formulário falhe antes
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email} ({self.get_user_type_display()})"
