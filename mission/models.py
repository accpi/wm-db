from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from player.models import Player


class Zone(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Mission(models.Model):
    title = models.CharField(max_length=100)
    lfg = models.CharField(max_length=100)
    aar = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    level = models.IntegerField(default=1)
    dm = models.ForeignKey(Player, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mission-detail', kwargs={'pk':self.pk})