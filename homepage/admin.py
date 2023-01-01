from django.contrib import admin
from .models import Course, Term, Video, VideoTag

# Register your models here.
admin.site.register(Course)
admin.site.register(Term)
admin.site.register(Video)
admin.site.register(VideoTag)
