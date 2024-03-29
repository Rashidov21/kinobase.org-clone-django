# Generated by Django 3.2.6 on 2022-05-07 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Actor name')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('age', models.PositiveIntegerField(default=0, verbose_name='Actor age')),
                ('image', models.ImageField(upload_to='actor_images/', verbose_name='Actor image')),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category name')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Genre name')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Movie title')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('short_description', models.CharField(max_length=550, verbose_name='Short title')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('rating', models.FloatField(default=0)),
                ('quality', models.CharField(max_length=50, verbose_name='Quality')),
                ('duration', models.CharField(max_length=50, verbose_name='Duration')),
                ('actors', models.ManyToManyField(related_name='movie_actors', to='movie.Actor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movie_category', to='movie.category')),
                ('genres', models.ManyToManyField(related_name='movie_genres', to='movie.Genre')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]
