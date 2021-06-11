from django import forms
from recipe_app.models import Author

# added everything here


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    time_required = forms.CharField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)


class AuthorForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    bio = forms.CharField(max_length=250)


class RecipeEdit(forms.Form):
    title = forms.CharField(max_length=50)
    time_required = forms.CharField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)
