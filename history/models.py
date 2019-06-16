from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mission.models import Mission
from player.models import Character


class History(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    death_bool = models.BooleanField()

    def __str__(self):
        return self.mission.title + ' - ' + self.character.name

    #def get_absolute_url(self):
        #return reverse('history-detail', kwargs={'pk':self.pk})