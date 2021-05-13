from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
Author:
- Name(CharField)
- Bio(TextField)


Recipe:
- Title(CharField)
- Author(ForeignKey)
- Description(TextField)
- TimeRequired(CharField)(for example, "One Hour")
- Instructions(TextField)
"""

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Recipes(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time_required = models.CharField(max_length=45)
    description = models.TextField()
    instructions = models.TextField()