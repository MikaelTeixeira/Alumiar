from django.db import models
from django.conf import settings

class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    nome_completo = models.CharField(max_length=150)
    comprovante_matricula = models.FileField(upload_to="comprovantes/")
    documento_oficial = models.FileField(upload_to="documentos/")
    foto_perfil = models.ImageField(upload_to="students/fotos/")

    crp_supervisor = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="CRP do seu supervisor psicológico"
    )

    def __str__(self):
        return f"Perfil Estudante: {self.nome_completo}"
