from django.contrib import admin

from movie.models import Movie
from movie.forms import MovieForm


class MovieAdmin(admin.ModelAdmin):
    # form = MovieForm
    pass

 
admin.site.register(Movie, MovieAdmin)