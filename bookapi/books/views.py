from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def book_list(request):
    """
    List all books.
    """
    books = Book.objects.all()

    title = request.query_params.get('title', None)
    author = request.query_params.get('author', None)
    genre = request.query_params.get('genre', None)
    published_year = request.query_params.get('published_year', None)

    if title:
        books = books.filter(title__icontains=title)
    if author:
        books = books.filter(author__id=author)
    if genre:
        books = books.filter(genre__icontains=genre)
    if published_year:
        books = books.filter(published_year=published_year)

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_detail(request, pk):
    """
    Retrieve a specific book.
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])
def create_book(request):
    """
    Create a new book.
    """
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)