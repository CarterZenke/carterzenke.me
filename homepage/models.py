from django.db import models


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


class Video(models.Model):
    title = models.CharField(max_length=256)
    source = models.URLField(max_length=128)
    slides = models.URLField(max_length=512)
    source = models.URLField(max_length=512)


class VideoTag(models.Model):
    name = models.CharField(max_length=64)
    video = models.ManyToManyField(to=Video, related_name="tags", related_query_name="tags")
