# Generated by Django 5.0.2 on 2024-02-18 01:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0003_anime_current_episode_anime_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='name',
        ),
        migrations.AddField(
            model_name='anime',
            name='anime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='anime.animes'),
        ),
    ]
