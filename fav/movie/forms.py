from django import forms

from movie.models import Movie


class MovieForm(forms.ModelForm):
    # movie_name = forms.CharField(required = True)

    class Meta:
        model = Movie


    def clean_name(self):
        movie_name = self.cleaned_data['name'].strip()

        if len(movie_name) < 3:
            raise forms.ValidationError("Not enough words!")

        return movie_name
