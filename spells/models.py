from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Spell(models.Model):
    level = models.IntegerField(default=0, validators=[MaxValueValidator(9), MinValueValidator(0)])
    name = models.CharField(max_length=64)
    casting_time = models.CharField(max_length=32)
    range = models.CharField(max_length=32)
    duration = models.CharField(max_length=32)
    higher_levels = models.CharField(max_length=512)
    attack = models.CharField(max_length=32)
    saving_throw = models.CharField(max_length=32)
    damage_type = models.CharField(max_length=32)
    school = models.CharField(max_length=32)
    components = models.CharField(max_length=32)
    source = models.CharField(max_length=64)