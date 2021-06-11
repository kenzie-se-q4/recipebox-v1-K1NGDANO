"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipe_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('recipes/add/', views.AddRecipe.as_view()),
    path('author/add/', views.AddAuthor.as_view()),
    path('author/<int:author_id>/', views.author_detail),
    path('recipes/<int:recipe_id>/', views.recipes_detail),
    path('recipes/<int:recipe_id>/edit/', views.EditRecipe.as_view()),
    path('recipes/<int:recipe_id>/favorite/', views.favorite),
    path('recipes/<int:recipe_id>/remove_fav/', views.favorite),
    path('admin/', admin.site.urls),
]
