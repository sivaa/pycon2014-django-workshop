from django.shortcuts import render
from django.http import HttpResponse
from django.db.utils import IntegrityError

from movie.models import Movie


def _get_movies():
    return Movie.objects.all()

def movies(request):
    if request.method == 'GET':
        return render(request, 
                      "movies.html",
                      {"movies"  : _get_movies()})

    if request.method == 'POST':
        movie_name = request.POST.get("movie_name")
        movie_name = movie_name.strip()

        if not movie_name:
            message = "Enter a Movie Name"
        elif len(movie_name) < 3:
            message = "Not enough words!"
        else:
            try:
                Movie.objects.create(name = movie_name)
                message = "Movie '{}' is added successfully.".format(movie_name)
            except IntegrityError:
                message =  "Movie '{}' is already exists.".format(movie_name)

        return render(request, 
                      "movies.html",
                      {"message" : message,
                       "movies"  : _get_movies()})

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
                       "movies"  : _get_movies()})

    return ("Invalid Request")
