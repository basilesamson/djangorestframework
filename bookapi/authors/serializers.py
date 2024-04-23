from rest_framework import serializers
from .models import Authors

from books.serializers import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Authors
        fields = ['id', 'name', 'books']