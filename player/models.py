from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.functions import Lower


class Race(models.Model):
    race = models.CharField(max_length=50)
    subrace = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.race + ' (' + self.subrace + ')'


class Player(models.Model):
    reddit = models.CharField(max_length=50)
    discord = models.CharField(max_length=50)
    dm_bool = models.BooleanField()

    class Meta:
        ordering = [Lower('reddit')]

    def __str__(self):
        return self.reddit

    def get_absolute_url(self):
        return reverse('player-detail', kwargs={'pk':self.pk})


class Character(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='default name')
    race = models.ForeignKey(Race, on_delete=models.CASCADE, default=1)
    alive = models.BooleanField(default=1)
    barbarian = models.IntegerField(default=0)
    bard = models.IntegerField(default=0)
    cleric = models.IntegerField(default=0)
    druid = models.IntegerField(default=0)
    fighter = models.IntegerField(default=0)
    monk = models.IntegerField(default=0)
    paladin = models.IntegerField(default=0)
    ranger = models.IntegerField(default=0)
    rogue = models.IntegerField(default=0)
    sorcerer = models.IntegerField(default=0)
    warlock = models.IntegerField(default=0)
    wizard = models.IntegerField(default=0)

    class Meta:
        ordering = [Lower('name')]

    def __str__(self):
        return self.name + " - " + self.player.reddit
