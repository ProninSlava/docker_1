from django.db import models

class Weapon(models.Model):
    title = models.CharField(max_length=50)
    strength = models.IntegerField()
    protection = models.IntegerField()
