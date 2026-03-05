from django.urls import include, path
from .views import JokeListView,JokeDetailView, TagListView, CategoryListView, joke, TagDetailView, CategoryDetailView

app_name = 'api'

urlpatterns = [
    path('jokes/', JokeListView.as_view(), name='joke'),
    path('tags/', TagListView.as_view(), name='tag'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag'),

    path('category/', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),

    path('jokes/<int:pk>/', joke, name='joke-detail'),
   # path('jokes/<int:pk>/', JokeDetailView.as_view(), name='joke-detail'),
]
