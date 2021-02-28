from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView

from .models import *


class GenreListView(ListView):
    model = Genre
    template_name = 'index.html'
    context_object_name = 'genres'


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genre-details.html'
    context_object_name = 'genre'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['movies'] = Movie.objects.filter(genre_id=self.slug)
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie-detail.html'
    context_object_name = 'movie'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.pk = kwargs.get('pk', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['actors'] = Actor.objects.filter(movie_id=self.pk)
        return context
