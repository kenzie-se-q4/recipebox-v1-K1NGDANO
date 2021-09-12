from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from recipe_app.models import Author, Recipes
from recipe_app.forms import AddRecipesForm, AddAuthorForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def index(request):
    recipes = Recipes.objects.all()
    return render(request, 'index.html', {'recipes': recipes})
# @login_required
def author_detail(request, author_id: int):
    my_author = Author.objects.get(id=author_id)
    author_post = Recipes.objects.filter(author=my_author)
    return render(request, 'author_detail.html', {'author': my_author, 'recipes': author_post})
# @login_required
def recipes_detail(request, recipe_id: int):
    recipe = Recipes.objects.get(id=recipe_id)
    return render(request, 'recipes_detail.html', {'recipes': recipe})


# @login_required
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

# @staff_member_required
def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            myuser = User.objects.create_user(username=data['username'], password=data['password'])
            Author.objects.create(name=data['name'], bio=data['bio'], user=myuser)
            return HttpResponseRedirect(reverse('home'))

    form = AddAuthorForm()
    return render(request, 'generic_form.html', {'form': form})


def login_views(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                if request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                else:
                    return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

@login_required
def logout_views(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))