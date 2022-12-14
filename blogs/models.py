from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
import os

endpoint = os.environ.get("ENDPOINT")


class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=2500, null=False, blank=False)
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date published"
    )
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from="title")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"blogs/{self.pk}/"

    @property
    def endpoint(self):
        absolute_url = self.get_absolute_url()
        return f"{endpoint}/{absolute_url}"
