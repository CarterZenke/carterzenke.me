from .helpers import get_yt_thumbnail

from django.core.files.base import ContentFile
from django.db import models

# Django Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

from io import BytesIO


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
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True)
    slides = models.URLField(max_length=512, blank=True)
    source = models.CharField(max_length=16)
    code = models.URLField(max_length=512, blank=True)
    tags = models.ManyToManyField(
        to=VideoTag, related_name="video", related_query_name="video", blank=True
    )
    last_updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        super(Video, self).__init__(*args, **kwargs)
        self.old_source = self.source

    def __str__(self):
        return f"{self.id}: {self.title}"


# Get YouTube thumbnail for source on update
@receiver(post_save, sender=Video)
def update_thumbnail(sender, instance, created, **kwargs):
    
    if not instance.source:
        return

    if instance.old_source != instance.source or (not instance.thumbnail):
        
        instance.old_source = instance.source
        
        if thumbnail := get_yt_thumbnail(instance.source):
            f = BytesIO()
            try:
                thumbnail.save(f, format="JPEG")
                instance.thumbnail.save(f"{instance.source}.jpg", ContentFile(f.getvalue()), save=True)
            finally:
                f.close()
        