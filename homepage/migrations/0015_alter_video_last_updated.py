# Generated by Django 4.1.4 on 2023-05-07 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0014_alter_video_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
