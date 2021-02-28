from django.contrib import admin

from video.models import Movie, Genre, Actor, Review


class GenreAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'slug')
    list_display_links = ('title',)


admin.site.register(Review)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Genre, GenreAdmin)
