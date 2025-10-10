from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
import re
from  .validators_models import *
from .super_user_models import *


class PatientProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    nome_completo = models.CharField(max_length=75, validators=[validate_name])

    foto_perfil = models.FileField(
        upload_to="fotos_perfil/",
        validators=[validate_image_or_pdf, validate_file_size]
    )

    def __str__(self):
        return f"Paciente: {self.nome_completo}"
