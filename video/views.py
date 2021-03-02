from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.base import View

from .forms import CreateMovieForm, ReviewForm, GenreForm
from .models import *


class GenreListView(ListView):
    model = Genre
    template_name = 'video/index.html'
    context_object_name = 'genres'


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'video/genre-details.html'
    context_object_name = 'genre'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        genre = self.get_object()
        context['movies'] = Movie.objects.filter(genre__in=[genre])
        return context


class CreateReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'video/movie-detail.html'


class CreateGenreView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'video/genre-create.html'
    success_url = reverse_lazy('index')


class MovieDetailView(View):
    def get(self, request, *args, **kwargs):
        form = ReviewForm
        self.pk = kwargs.get('pk', None)
        movie = get_object_or_404(Movie, pk=self.pk)
        comments = list(Review.objects.filter(movie_id=movie))
        comments.reverse()
        if len(comments) > 20:
            comments = comments[:20]
        return render(request, 'video/movie-detail.html', {'form': form, 'movie': movie, 'comments': comments})

    def post(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse_lazy('login'))
        form = ReviewForm(request.POST)
        form.save()
        return redirect(reverse_lazy('movie-detail', kwargs={'pk': kwargs.get('pk', None)}))


class DeleteMovieView(DeleteView):
    model = Movie
    template_name = 'video/delete-movie.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        self.object = None
        user = request.user
        if not user.is_superuser and not user.is_staff:
            return render(request, 'video/index.html')
        return super().get(request, *args, **kwargs)


class CreateMovieView(CreateView):
    model = Movie
    form_class = CreateMovieForm
    template_name = 'video/create-movie.html'
    success_url = reverse_lazy('index')


    def get(self, request, *args, **kwargs):
        self.object = None
        user = request.user
        if not user.is_superuser and not user.is_staff:
            return render(request, 'video/index.html')
        return super().get(request, *args, **kwargs)


class EditMovieView(UpdateView):
    model = Movie
    form_class = CreateMovieForm
    template_name = 'video/create-movie.html'








