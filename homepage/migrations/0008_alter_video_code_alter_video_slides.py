# Generated by Django 4.1.4 on 2022-12-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0007_remove_videotag_video_video_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="code",
            field=models.URLField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name="video",
            name="slides",
            field=models.URLField(blank=True, max_length=512),
        ),
    ]