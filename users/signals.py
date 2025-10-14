from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser, PatientProfile, PsychologistProfile, StudentProfile

def atualizar_nome_usuario(user, nome_completo):
    """Atualiza automaticamente first_name e last_name com base no nome completo."""
    if nome_completo:
        partes = nome_completo.strip().split(" ", 1)
        user.first_name = partes[0]
        user.last_name = partes[1] if len(partes) > 1 else ""
        user.save()

@receiver(post_save, sender=PatientProfile)
def sync_patient_profile(sender, instance, **kwargs):
    atualizar_nome_usuario(instance.user, instance.nome_completo)

@receiver(post_save, sender=PsychologistProfile)
def sync_psychologist_profile(sender, instance, **kwargs):
    atualizar_nome_usuario(instance.user, instance.nome_completo)

@receiver(post_save, sender=StudentProfile)
def sync_student_profile(sender, instance, **kwargs):
    atualizar_nome_usuario(instance.user, instance.nome_completo)
