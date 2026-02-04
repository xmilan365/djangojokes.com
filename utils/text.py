# common/utils/text.py

import random
import string
from django.utils.text import slugify


def unique_slug(text, model, num_chars=50):
    """
    Generate a slug (max length: num_chars) that is unique for the given model.

    Args:
        text (str): The string to convert into a slug.
        model: The Django model used to check slug uniqueness.
        num_chars (int): Maximum length of the slug.

    Returns:
        str: A unique slug.
    """
    slug = slugify(text)[:num_chars].strip("-")

    while model.objects.filter(slug=slug).exists():
        slug = slug[:39].strip("-") + "-" + random_string(10)

    return slug


def random_string(length=10):
    """
    Generate a random lowercase string.

    Args:
        length (int): Number of characters.

    Returns:
        str: Random string of lowercase letters.
    """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))
