import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='covers/', blank=True)


def _str_(self):
    return self.title


def get_absolute_url(self):
    return reverse('book_detail', kwargs={'pk': str(self.pk)})


class Review(models.Model):
    books = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def _str_(self):
        return self.review
