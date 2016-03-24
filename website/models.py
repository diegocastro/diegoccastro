from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()
    short_description = models.CharField(max_length=255, db_index=True)
    text = models.TextField()
    published_date = models.DateTimeField(null=True, blank=True, default=None)
    language = models.CharField(max_length=5, choices=settings.LANGUAGES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title
