# Generated by Django 3.2.6 on 2022-05-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_likedmovielist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likedmovielist',
            name='movie',
        ),
        migrations.AddField(
            model_name='likedmovielist',
            name='movie',
            field=models.ManyToManyField(related_name='user_liked_movies', to='movie.Movie'),
        ),
    ]
