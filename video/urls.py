from django.urls import path
from . import views


urlpatterns = [
    path('video/', views.GenreListView.as_view(), name='index'),
    path('genre/<str:slug>/', views.GenreDetailView.as_view(), name='genre-detail'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
]