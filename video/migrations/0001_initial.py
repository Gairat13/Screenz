# Generated by Django 3.1 on 2021-03-01 05:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='genres')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tagline', models.CharField(blank=True, max_length=200, null=True)),
                ('video', models.FileField(upload_to='video')),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='movies')),
                ('world_premiere', models.DateField(default=datetime.date.today)),
                ('budget', models.PositiveBigIntegerField(default=0, help_text='specify the amount in dollars')),
                ('gross_in_usa', models.PositiveBigIntegerField(default=0, help_text='specify the amount in dollars')),
                ('gross_in_the_world', models.PositiveBigIntegerField(default=0, help_text='specify the amount in dollars')),
                ('country', models.CharField(default='USA', max_length=100)),
                ('genre', models.ManyToManyField(to='video.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='video.movie')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='video.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=60, null=True)),
                ('role', models.CharField(choices=[('actor', 'actor'), ('director', 'director')], max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='authors')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actors', to='video.movie')),
            ],
        ),
    ]
