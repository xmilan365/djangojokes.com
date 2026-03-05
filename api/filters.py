from django_filters import rest_framework as filters
from jokes.models import Joke, Category, Tag

class JokeFilter(filters.FilterSet):
    question = filters.CharFilter(field_name="question", lookup_expr='icontains')
        
    answer = filters.CharFilter(field_name="answer", lookup_expr='icontains')

    category = filters.CharFilter(field_name="category", lookup_expr='icontains')

    tags = filters.CharFilter(field_name="tags", lookup_expr='icontains')

    created = filters.DateTimeFilter(field_name="created", lookup_expr='gte')

    class Meta:
        model = Joke
        fields = ['question',  'answer', 'category', 'tags', 'created']
