from django.shortcuts import render
from recipe_app.models import Author, Recipes

# Create your views here.
def index(request):
    recipes = Recipes.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def author(request, author_id: int):
    author = Author.objects.get(id=author_id)
    return render(request, 'author.html', {'author': author, 'recipes': recipes})

def recipes(request, recipe_id: int):
    recipe = Recipes.objects.get(id=recipe_id)
    return render(request, 'recipes.html', {'recipes': recipes})