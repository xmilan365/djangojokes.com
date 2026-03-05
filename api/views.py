from jokes.models import Joke, Category, Tag
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import JokeSerializer, TagSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .filters import JokeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_api_key.permissions import HasAPIKey



# function-based view (aka FBV)

@api_view(['GET'])
def joke(request, pk):
    """
    Function-based view to retrieve one joke.
    """
    joke = get_object_or_404(Joke, id=pk)
    serializer = JokeSerializer(joke, context={'request': request})
    return Response(serializer.data)


class JokeListView(ListAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = JokeFilter
    permission_classes = [HasAPIKey]

class JokeDetailView(RetrieveAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagDetailView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer