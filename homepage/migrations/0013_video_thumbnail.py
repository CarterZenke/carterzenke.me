# Generated by Django 4.1.4 on 2023-02-18 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0012_alter_video_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="thumbnail",
            field=models.ImageField(default=0, upload_to="thumbnails/"),
            preserve_default=False,
        ),
    ]
