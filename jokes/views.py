from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from .models import Joke

# Create your views here.
class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']