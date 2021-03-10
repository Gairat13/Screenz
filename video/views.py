from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.test.testcases import to_list
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views.generic.base import View


from .forms import CreateMovieForm, ReviewForm, GenreForm
from .models import *


class GenreListView(ListView):
    model = Genre
    template_name = 'video/index.html'
    context_object_name = 'genres'

    def get_template_names(self):
        template_name = super().get_template_names()
        search = self.request.GET.get('q', None)
        if search:
            template_name = 'video/search.html'
        return template_name

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        search = self.request.GET.get('q', None)
        print(search)
        if search:
            context['movies'] = Movie.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
            context['len'] = len(context['movies'])
        return context


def GenreDetailView(request, *args, **kwargs):
    slug = kwargs.get('slug', None)
    movies = Movie.objects.filter(genre=slug)
    genre = Genre.objects.get(slug=slug)
    paginator = Paginator(movies, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'video/genre-details.html', locals())


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
        genre = Genre.objects.filter(movie=movie).first
        comments = list(Review.objects.filter(movie_id=movie))
        comments.reverse()
        if len(comments) > 20:
            comments = comments[:20]
        return render(request, 'video/movie-detail.html', locals())

    def post(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse_lazy('login'))
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('movie-detail', kwargs={'pk': kwargs.get('pk', None)}))


def add_favorite(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        if movie.favorites.filter(pk=request.user).exists():
            movie.favorites.remove(request.user)
        movie.favorites.add(request.user)
        return redirect(reverse_lazy('movie-detail', kwargs={'pk': pk}))
    return redirect(reverse_lazy('login'))


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





