from django.db import models


class PublishedPostManager(models.Manager):
    """
    Custom manager to return only published blog posts.
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class RecentPostManager(models.Manager):
    """
    Custom manager to return recent blog posts.
    """

    def get_queryset(self):
        return super().get_queryset().order_by("-created_at")[:5]
