from django.urls import path
from . import views


urlpatterns = [
    path('', views.GenreListView.as_view(), name='index'),
    path('genre/<str:slug>/', views.GenreDetailView, name='genre-detail'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('create-movie/', views.CreateMovieView.as_view(), name='create-movie'),
    path('create-genre/', views.CreateGenreView.as_view(), name='create-genre'),
    path('delete-movie/<int:pk>/', views.DeleteMovieView.as_view(), name='delete-movie'),
    path('edit-movie/<int:pk>/', views.EditMovieView.as_view(), name='edit-movie'),
    path('edit-movie/<int:pk>/', views.EditMovieView.as_view(), name='edit-movie'),
    path('movie-favorite/<int:pk>/', views.add_favorite, name='favorite'),
]
