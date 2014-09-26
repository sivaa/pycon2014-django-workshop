from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from myapp.models import Movie


def home_page(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        return render(request, "home.html", {'movies': movies})
    elif request.method == 'POST':
        movie_name = request.POST.get('movie_name', "")
        Movie.objects.create(name = movie_name)
        return redirect("/")
    else:
        return HttpResponse("NOT SUPPORTED")