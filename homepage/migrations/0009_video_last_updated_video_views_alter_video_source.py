# Generated by Django 4.1.4 on 2022-12-25 22:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0008_alter_video_code_alter_video_slides"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="last_updated",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="video",
            name="views",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="video",
            name="source",
            field=models.CharField(max_length=16),
        ),
    ]
