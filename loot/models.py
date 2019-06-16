from django.db import models
from mission.models import Mission


class Rarity(models.Model):
    rarity = models.CharField(max_length=15)

    def __str__(self):
        return self.rarity


class Type(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class Loot(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    attunement = models.BooleanField(default=False)
    text = models.TextField()
    blurb = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' (' + self.type.type + ') - ' + self.mission.title
