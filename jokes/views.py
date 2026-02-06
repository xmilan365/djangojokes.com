from django.shortcuts import render
from django.views.generic import (DetailView, ListView, CreateView, UpdateView, DeleteView)
from .models import Joke
from django.urls import reverse_lazy
from .forms import JokeForm

# Create your views here.
class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeCreateView(CreateView):
    model = Joke
    form_class = JokeForm
    
class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')