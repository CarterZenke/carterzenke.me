from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=128)
    number = models.CharField(max_length=32)
    term = models.ForeignKey(
        "Term",
        on_delete=models.CASCADE,
    )
    school = models.CharField(max_length=64)
    role = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id}: {self.number}, {self.term}"


class Term(models.Model):
    semester = models.CharField(
        max_length=6,
        choices=[
            ("Winter", "Winter"),
            ("Spring", "Spring"),
            ("Summer", "Summer"),
            ("Fall", "Fall"),
        ],
        default="Winter",
    )
    year = models.IntegerField()

    def __str__(self):
        return f"{self.get_semester_display()} {self.year}"
