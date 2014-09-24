from django import forms


class MovieForm(forms.Form):
    movie_name = forms.CharField(required = False)

