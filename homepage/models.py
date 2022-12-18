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


class VideoTag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"Tag: {self.name}"


class Video(models.Model):
    title = models.CharField(max_length=256)
    source = models.URLField(max_length=128)
    slides = models.URLField(max_length=512, blank=True)
    code = models.URLField(max_length=512, blank=True)
    tags = models.ManyToManyField(to=VideoTag, related_name="video", related_query_name="video")

    def __str__(self):
        return f"{self.id}: {self.title}"