from django.db import models
from django.contrib.auth import get_user_model
from .validators_models import validate_name, validate_image_or_pdf, validate_file_size

CustomUser = get_user_model()

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=75, validators=[validate_name])

    comprovante_matricula = models.FileField(
        upload_to="matriculas/",
        validators=[validate_image_or_pdf, validate_file_size]
    )

    documento_oficial = models.FileField(
        upload_to="documentos/",
        validators=[validate_image_or_pdf, validate_file_size]
    )

    foto_perfil = models.ImageField(
        upload_to="fotos_perfil/",
        validators=[validate_image_or_pdf, validate_file_size]
    )

    def __str__(self):
        return f"Estudante: {self.nome_completo}"
