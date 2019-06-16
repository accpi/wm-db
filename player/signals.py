from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Character, Player


@receiver(post_save, sender=Player)
def create_player(sender, instance, created, **kwargs):
    if created:
        Character.objects.create(player=instance)
