from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import History
from mission.models import Mission
from player.models import Player
