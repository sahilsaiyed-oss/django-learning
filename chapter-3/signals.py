from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import BlogPost


@receiver(post_save, sender=BlogPost)
def auto_generate_slug(sender, instance, created, **kwargs):
    """
    Automatically generate slug for BlogPost after creation
    if not already provided.
    """

    if created and not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save(update_fields=["slug"])
