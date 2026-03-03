from django.urls import include, path
from .views import JokeListView

app_name = 'api'

urlpatterns = [
    path('jokes', JokeListView.as_view(), name='joke')
]
