from django.db import models
from django.contrib.auth import get_user_model
from .validators_models import validate_name, validate_image_or_pdf, validate_file_size

CustomUser = get_user_model()

class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=75, validators=[validate_name])

    foto_perfil = models.FileField(
        upload_to="fotos_perfil/",
        validators=[validate_image_or_pdf, validate_file_size]
    )

    def __str__(self):
        return f"Paciente: {self.nome_completo}"
