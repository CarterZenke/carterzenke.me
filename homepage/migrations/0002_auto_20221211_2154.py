# Generated by Django 3.2.9 on 2022-12-11 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('Winter', 'Winter'), ('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall')], default='Winter', max_length=6)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='year',
        ),
        migrations.AlterField(
            model_name='course',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.term'),
        ),
    ]