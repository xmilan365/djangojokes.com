from django.db import models
from django.urls import reverse

from common.utils.text import unique_slug


class Joke(models.Model):
    question = models.TextField(max_length=200, help_text="The first part of the joke")
    answer = models.TextField(max_length=100, blank=True, help_text="The second part of the joke")

    slug = models.SlugField(
        max_length=50,
        unique=True,
        null=False,
        editable=False,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("jokes:detail", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(str(self), self.__class__)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
