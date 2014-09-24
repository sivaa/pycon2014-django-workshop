from django import forms


class MovieForm(forms.Form):
    movie_name = forms.CharField(required = True)

    def clean_movie_name(self):
        movie_name = self.cleaned_data['movie_name'].strip()

        if len(movie_name) < 3:
            raise forms.ValidationError("Not enough words!")

        return movie_name
