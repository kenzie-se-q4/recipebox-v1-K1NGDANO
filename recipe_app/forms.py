"""

for to add new recipes
for to add new authors

- Title(CharField)
- Author(ForeignKey)
- Description(TextField)
- TimeRequired(CharField)(for example, "One Hour")
- Instructions(TextField)

"""

from django import forms
from recipe_app.models import Author

class AddRecipesForm(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=40)
    bio = forms.CharField(max_length=100)
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
