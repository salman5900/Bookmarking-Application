from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import IntegrityError, transaction

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    folder = models.ForeignKey('File', on_delete=models.SET_NULL, null=True, blank=True, related_name='bookmarks')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Bookmark.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug

        try:
            with transaction.atomic():
                super().save(*args, **kwargs)
        except IntegrityError:
            # Retry with new slug
            counter = 1
            base_slug = slugify(self.title)
            while True:
                unique_slug = f"{base_slug}-{counter}"
                if not Bookmark.objects.filter(slug=unique_slug).exists():
                    self.slug = unique_slug
                    break
                counter += 1
            super().save(*args, **kwargs)

    