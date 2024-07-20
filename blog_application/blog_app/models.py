"""This module provides models for blog app."""
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    """Model to store post information."""
    title = models.CharField(max_length=200, help_text=_("Title of post."))
    content = models.TextField(max_length=500, help_text=_("Content of post."))
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_("Author of post."))
    published_date = models.DateTimeField(auto_now_add=True, help_text=_("Published date of post."))
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True, help_text=_("Likes of post."))

    def __str__(self) -> str:
        """Return string representation of post."""
        return str(self.title)

    def number_of_likes(self) -> int:
        """Return number of likes of post."""
        return self.likes.count()


class Comment(models.Model):
    """Model to store comment information about post."""
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, help_text=_("Post of comment."))
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_("Author of comment."))
    text = models.TextField(max_length=100, help_text=_("Content of comment."))
    created_date = models.DateTimeField(auto_now_add=True, help_text=_("Created date of comment."))

    def __str__(self) -> str:
        """Return string representation of comment."""
        return str(self.text)
