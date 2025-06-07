from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import LegalEntity

User = get_user_model()

@receiver(post_save, sender=User)
def create_default_entity(sender, instance, created, **kwargs):
    """Crée une LegalEntity PERSON pour chaque nouvel utilisateur."""
    if created:
        LegalEntity.objects.create(
            user=instance,
            name=instance.get_full_name() or instance.username,
            type=LegalEntity.PERSON,
        )
