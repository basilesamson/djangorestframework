from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Authors
from .serializers import AuthorSerializer

@api_view(['GET'])
def author_list(request):
    """
    List all authors.
    """
    authors = Authors.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def author_detail(request, pk):
    """
    Retrieve a specific author.
    """
    try:
        author = Authors.objects.get(pk=pk)
    except Authors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AuthorSerializer(author)
    return Response(serializer.data)

@api_view(['POST'])
def create_author(request):
    """
    Create a new author.
    """
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)