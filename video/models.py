from datetime import date, datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

User = get_user_model()

# Create your models here.
from pytils.translit import slugify

CHOICES = (
    ('actor', 'actor'),
    ('director', 'director'),
)


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(primary_key=True, max_length=50)
    image = models.ImageField(upload_to='genres', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    video = models.FileField(upload_to='video')
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    description = models.TextField()
    image = models.ImageField(upload_to='movies')
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveBigIntegerField(default=0, help_text="specify the amount in dollars")
    gross_in_usa = models.PositiveBigIntegerField(default=0, help_text="specify the amount in dollars")
    gross_in_the_world = models.PositiveBigIntegerField(default=0, help_text="specify the amount in dollars")
    country = models.CharField(max_length=100, default='USA')
    favorites = models.ManyToManyField(User, related_name='movies')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('movie-detail', kwargs={'pk': self.pk})


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    role = models.CharField(max_length=20, choices=CHOICES)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='actors')
    image = models.ImageField(upload_to='authors', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=2000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    created = models.DateField(default=date.today)

    def __str__(self):
        return f'{self.user} :\n {self.text} \n {self.created}'

