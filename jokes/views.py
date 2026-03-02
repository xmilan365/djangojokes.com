from django.shortcuts import render
from django.views.generic import (DetailView, ListView, CreateView, UpdateView, DeleteView)
from .models import Joke
from django.urls import reverse_lazy
from .forms import JokeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


# Create your views here.
class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Joke
    form_class = JokeForm
    success_message = 'Joke created.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class JokeUpdateView(SuccessMessageMixin, UpdateView):
    model = Joke
    form_class = JokeForm
    success_message = 'Update Successful'

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')
