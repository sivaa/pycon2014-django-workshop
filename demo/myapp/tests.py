from django.test import TestCase
from django.core.urlresolvers import resolve
from myapp.views import home_page
from django.http.request import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_home_page_url_resolve(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_html_content(self):
        request = HttpRequest()
        request.method = 'GET'
        response = home_page(request)
        expected_html = render_to_string("home.html")
        self.assertEqual(response.content, expected_html)

    def test_movie_save_post_content_and_return(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['movie_name'] = 'Troy'

        home_page(request)

        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.first().name, "Troy")

    def test_movie_save_post_content_and_redirect(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['movie_name'] = 'Troy'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], "/")

    def test_movie_no_add_during_get_request(self):
        request = HttpRequest()
        request.method = 'GET'

        home_page(request)

        self.assertEqual(Movie.objects.count(), 0)

    def test_movie_list_in_table(self):
        Movie.objects.create(name = "Troy")
        Movie.objects.create(name = "Terminator")

        request = HttpRequest()
        request.method = 'GET'
        response = home_page(request)

        self.assertIn("Troy", response.content)
        self.assertIn("Terminator", response.content)

from myapp.models import Movie

class MovieModelTest(TestCase):

    def test_save_and_retrieve_movies(self):
        movie_troy = "Troy"
        movie_terminator = "Terminator"

        Movie.objects.create(name = movie_troy)
        Movie.objects.create(name = movie_terminator)

        movies = Movie.objects.all()

        self.assertEqual(movies.count(), 2)

        self.assertEqual(movie_troy, movies[0].name)
        self.assertEqual(movie_terminator, movies[1].name)

