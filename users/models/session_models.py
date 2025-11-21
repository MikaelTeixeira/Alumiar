from django.db import models
from django.utils import timezone
from users.models import CustomUser, PatientProfile


class Consulta(models.Model):
    STATUS_CHOICES = [
        ('AGENDADA', 'Agendada'),
        ('REALIZADA', 'Realizada'),
        ('CANCELADA', 'Cancelada'),
    ]

    profissional = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='consultas_realizadas',
        limit_choices_to={'user_type__in': ['PSY', 'STD']},
    )

    paciente = models.ForeignKey(
        PatientProfile,
        on_delete=models.CASCADE,
        related_name='consultas_paciente'
    )

    data_hora = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='AGENDADA'
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['data_hora']
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        data_formatada = timezone.localtime(self.data_hora).strftime('%d/%m/%Y %H:%M')
        return f"Consulta de {self.paciente} com {self.profissional} em {data_formatada}"
