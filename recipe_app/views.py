from django.shortcuts import render
from recipe_app.models import Author, Recipes

# Create your views here.
def index(request):
    recipes = Recipes.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def author_detail(request, author_id: int):
    my_author = Author.objects.get(id=author_id)
    author_post = Recipes.objects.filter(author=my_author)
    return render(request, 'author_detail.html', {'author': my_author, 'recipes': author_post})

def recipes_detail(request, recipe_id: int):
    recipe = Recipes.objects.get(id=recipe_id)
    return render(request, 'recipes_detail.html', {'recipes': recipe})