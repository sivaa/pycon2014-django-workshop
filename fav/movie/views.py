from django.shortcuts import render
from django.http import HttpResponse

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
        Movie.objects.create(name = movie_name)
        message = "Movie '{}' is added successfully.".format(movie_name)
        return render(request, 
                      "movies.html",
                      {"message" : message,
                       "movies"  : _get_movies()})

    return ("Invalid Request")

def remove_movie(request):
    if request.method == 'GET':
        movie_id = request.GET.get("id")
        movie    = Movie.objects.get(id = movie_id)
        movie.delete()
        message  = "Movie '{}' is removed successfully.".format(movie.name)
        return render(request, 
                      "movies.html",
                      {"message" : message,
                       "movies"  : _get_movies()})

    return ("Invalid Request")
