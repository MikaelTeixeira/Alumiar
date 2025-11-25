from django.db import models
from django.contrib.auth import get_user_model
from .validators_models import validate_name, validate_image_or_pdf, validate_file_size

CustomUser = get_user_model()

class PsychologistProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=75, validators=[validate_name])
    crp = models.CharField(max_length=8)

    documento_oficial = models.FileField(
        upload_to="documentos/",
        validators=[validate_image_or_pdf, validate_file_size]
    )

    curriculo = models.FileField(
        upload_to="curriculos/",
        validators=[validate_image_or_pdf, validate_file_size],
        blank=True, null=True
    )

    foto_perfil = models.FileField(
        upload_to="fotos_perfil/",
        validators=[validate_image_or_pdf, validate_file_size]
    )

    def __str__(self):
        return f"Psicólogo: {self.nome_completo}"
