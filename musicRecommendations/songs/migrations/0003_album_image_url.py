# Generated by Django 5.1.6 on 2025-02-11 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_song_featured_artists'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
