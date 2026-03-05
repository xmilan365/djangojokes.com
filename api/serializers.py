from rest_framework import serializers
from jokes.models import Joke, Tag, Category


class JokeSerializer(serializers.ModelSerializer):
    tags = serializers.HyperlinkedRelatedField(view_name='api:tag', many=True, read_only=True, )
    categories = serializers.HyperlinkedRelatedField(view_name='api:category', many=True, read_only=True, )

    class Meta:
        model = Joke
        fields = ('question', 'answer', 'created', 'updated', 'slug', 'tags', 'categories') 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category', )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)