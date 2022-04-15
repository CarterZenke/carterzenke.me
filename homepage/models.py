from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=128)
    number = models.CharField(max_length=32)
    term = models.CharField(max_length=16)
    year = models.IntegerField()
    school = models.CharField(max_length=64)
    role = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id}: {self.number}, {self.term} {self.year}"