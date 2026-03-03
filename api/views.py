from jokes.models import Joke, Category, Tag
from rest_framework.generics import ListAPIView
from .serializers import JokeSerializer


class JokeListView(ListAPIView):
    queryset = Joke.objects.all()[:10]
    serializer_class = JokeSerializer
