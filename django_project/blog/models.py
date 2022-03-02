from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# import json

# json_data = open("django_project//posts.json")
# posts = json.load(json_data)
# post = json.dumps(posts)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # If a user is deleted, we'll also delete their post.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
