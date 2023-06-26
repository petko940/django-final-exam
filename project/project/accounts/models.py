# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class ExtendedUser(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='extended_user'
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == slugify(self.user.username):
            self.slug = slugify(self.user.username)

        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     # if not self.slug:
    #     self.slug = slugify(self.user.username)
    #     super().save(*args, **kwargs)
