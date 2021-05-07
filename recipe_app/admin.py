from django.contrib import admin

from recipe_app.models import Author, Recipes

# Register your models here.
admin.site.register(Author)
admin.site.register(Recipes)