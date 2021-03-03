from django import forms
from video.models import Review, Movie, Genre


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user', 'movie', 'text')


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('title', 'image')


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'




