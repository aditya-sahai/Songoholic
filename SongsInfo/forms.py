from django import forms
# from django.contrib.auth.forms import UserCreationForm


class SongForm(forms.Form):
    name = forms.CharField(label="Song", max_length=50, required=True)