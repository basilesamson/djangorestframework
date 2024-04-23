from django.db import models

from authors.models import Authors

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Authors, related_name="books", on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    published_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title