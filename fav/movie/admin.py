from django.contrib import admin

from movie.models import Movie
from movie.forms import MovieForm


class MovieAdmin(admin.ModelAdmin):
    form = MovieForm

 
admin.site.register(Movie, MovieAdmin)