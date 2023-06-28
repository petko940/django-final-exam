from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class AllCpus(models.Model):
    brand = models.CharField(
        choices=(
            ('AMD', 'AMD'),
            ('Intel', 'Intel'),
        ),
        max_length=10,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    cores = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1, "asd"),
            MaxValueValidator(128),
        ],
    )
    threads = models.IntegerField(
        blank=True,
        null=True
    )
    max_turbo_frequency = models.FloatField(
        blank=True,
        null=True
    )
    base_frequency = models.FloatField(
        blank=True,
        null=True
    )
    tdp = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )
    cache = models.FloatField(
        blank=True,
        null=True
    )

