from django.shortcuts import render
from django.http import HttpResponse
from django.db.utils import IntegrityError

from movie.models import Movie
from movie.forms import MovieForm


def _get_movies():
    return Movie.objects.all()

def movies(request):
    if request.method == 'GET':
        return render(request, 
                      "movies.html",
                      {"movies"  : _get_movies(),
                       "form"    : MovieForm()})

    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie_name = form.cleaned_data["movie_name"].strip()

            try:
                Movie.objects.create(name = movie_name)
                message = "Movie '{}' is added successfully.".format(movie_name)
                form = MovieForm()
            except IntegrityError:
                message =  "Movie '{}' is already exists.".format(movie_name)
        else:
            message = "Please correct all the validation errors below."

        return render(request, 
                      "movies.html",
                      {"message" : message,
                       "movies"  : _get_movies(),
                       "form"    : form})

    return ("Invalid Request")

def remove_movie(request):
    if request.method == 'GET':
        movie_id = request.GET.get("id")
        try:
            movie    = Movie.objects.get(id = movie_id)
            movie.delete()
            message  = "Movie '{}' is removed successfully.".format(movie.name)
        except Movie.DoesNotExist as e:
            message = "Given movie does not exists."

        return render(request, 
                      "movies.html",
                      {"message" : message,
                       "movies"  : _get_movies(),
                       "form"    : MovieForm()})

    return ("Invalid Request")
