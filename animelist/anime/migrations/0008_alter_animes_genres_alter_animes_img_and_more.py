# Generated by Django 5.0.2 on 2024-02-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_alter_animes_genres_alter_animes_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animes',
            name='genres',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='animes',
            name='img',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='animes',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='animes',
            name='num_of_eps',
            field=models.IntegerField(),
        ),
    ]
