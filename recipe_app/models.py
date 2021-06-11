from django.db import models
from django.contrib.auth.models import AbstractUser

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

# had to edit the Author model since there was no login
# forms or any kind of thing like that


class Author(AbstractUser):
    bio = models.TextField()
    favorites = models.ManyToManyField('Recipes', symmetrical=False,
                                       related_name='author_favorites',
                                       blank=True)

    def __str__(self):
        return self.username


class Recipes(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time_required = models.CharField(max_length=45)
    instructions = models.TextField()
    favorites = models.ManyToManyField(Author, related_name='favorite_by',
                                       blank=True)
