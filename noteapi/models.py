from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField


def my_slugify_function(content):
    return content.replace(' ', '-').lower()

class Note(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', slugify_function=my_slugify_function)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title