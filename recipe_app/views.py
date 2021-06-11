from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from recipe_app.models import Author, Recipes
from recipe_app.forms import RecipeForm, AuthorForm, RecipeEdit, LoginForm
from django.views.generic import View

# Create your views here.


def index(request):
    recipes = Recipes.objects.all()
    authors = Author.objects.all()
    return render(request, 'index.html', {'recipes': recipes,
                                          'authors': authors})


def author_detail(request, author_id: int):
    my_author = Author.objects.get(id=author_id)
    author_post = Recipes.objects.filter(author=my_author)
    favorites = my_author.favorites.all()
    return render(request, 'author_detail.html', {'author': my_author,
                                                  'recipes': author_post,
                                                  'favorites': favorites})

# had to edit the function below to get this to work correctly


def recipes_detail(request, recipe_id: int):
    """
    Will grab the recipe you're looking at, then try to
    grab the favorites of the user who is logged in
    to show correct button for favoriting recipes. If
    no one is logged in, it will run the except part
    """
    recipe = Recipes.objects.get(id=recipe_id)
    try:
        account = Author.objects.get(id=request.user.id)
        fav_recipes = account.favorites.all()
        has_fav = account.favorites.filter(title=recipe.title)
        return render(request, 'recipes_detail.html', {'recipes': recipe,
                                                       'fav_recipes': fav_recipes,
                                                       'has_fav': has_fav})
    except Author.DoesNotExist:
        message = 'You are not logged in!'
        messages.info(request, message)
        return render(request, 'recipes_detail.html', {'recipes': recipe})

# there was no log in or any kind of forms or anything.
# added


class AddAuthor(View):
    """
    Renders the add author form and when
    posted, will create a new author object
    and direct user to login page.
    """

    def get(self, request):
        form = AuthorForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create_user(
                username=data['username'],
                password=data['password'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('login'))


def favorite(request, recipe_id: int):
    """
    Gets the current recipe the user is viewing
    and also gets the 'data' from the button
    selected and either adds the recipe to
    the authors favorites, or removes it.
    """
    recipe = Recipes.objects.get(id=recipe_id)
    account = Author.objects.get(id=request.user.id)
    query = request.GET.get('data')
    if query == 'fav':
        account.favorites.add(recipe)
        account.save()
        messages.info(request, 'You have added this recipe to your favorites!')
    if query == 'remove_fav':
        account.favorites.remove(recipe)
        account.save()
        messages.info(
            request, 'You have removed this recipe from you favorites!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class AddRecipe(View, LoginRequiredMixin):
    """
    Get function renders a form to add recipe.
    When submitted, the post function creates a
    recipe object and displays a success
    message on homepage after redirect.
    """

    def get(self, request):
        form = RecipeForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipes.objects.create(
                title=data['title'],
                author=request.user,
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            messages.info(request, 'You have successfully added a recipe!')
            return HttpResponseRedirect(reverse('home'))


class EditRecipe(View):
    """
    Get function renders a form that has
    the current objects values already
    entered in. Once submitted, the post
    function will replace object fields
    with new entries.
    """

    def get(self, request, recipe_id: int):
        item = Recipes.objects.get(id=recipe_id)
        form = RecipeEdit(initial={
            'title': item.title,
            'time_required': item.time_required,
            'instructions': item.instructions
        })
        return render(request, 'form.html', {'form': form})

    def post(self, request, recipe_id: int):
        item = Recipes.objects.get(id=recipe_id)
        form = RecipeEdit(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            item.title = data['title']
            item.time_required = data['time_required']
            item.instructions = data['instructions']
            item.save()
            messages.info(request, 'You have successfully edited the recipe!')
            return HttpResponseRedirect(reverse('home'))


class LoginUser(View):
    """
    Simple login class that will display
    a login form and authenticates username
    and password then displays a success
    message on homepage after redirect.
    """

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_user = authenticate(
                request, username=data['username'], password=data['password'])
            if my_user:
                login(request, my_user)
                messages.info(request, 'Thanks for logging in!')
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request, 'username or password not correct')
                return redirect('login')


def logout_user(request):
    """
    Simple logout function that
    will display a success message
    on homepage after redirect
    """
    logout(request)
    messages.info(request, 'You have logged out!')
    return HttpResponseRedirect(reverse('home'))
