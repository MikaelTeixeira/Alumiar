from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
import re
from .validators_models import *

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

    REQUIRED_FIELDS = ["email", "cpf", "data_nascimento", "senha_custom"]

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
