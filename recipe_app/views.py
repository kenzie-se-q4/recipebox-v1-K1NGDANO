from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_app.models import Author, Recipes
from recipe_app.forms import AddRecipesForm, AddAuthorForm

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



def add_recipes(request):
    if request.method == 'POST':
        form = AddRecipesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_post = Recipes.objects.create(
                title=data["title"],
                description=data["description"],
                time_required=data["time_required"],
                instructions=data["instructions"],
                author=data["author"],
            )
            return HttpResponseRedirect(reverse('home'))

    form =AddRecipesForm()
    return render(request, 'generic_form.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('home'))

    form = AddAuthorForm()
    return render(request, 'generic_form.html', {'form': form})