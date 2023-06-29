from django.contrib.auth.models import User
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


class CustomCpu(models.Model):
    name = models.CharField(
        max_length=30
    )
    manufacturer = models.CharField(
        max_length=30
    )
    clock_speed = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )
    number_of_cores = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(512),
        ]
    )
    cache_size = models.PositiveIntegerField()
    max_ram = models.CharField(
        choices=(
            ('1GB', '1GB'),
            ('2GB', '2GB'),
            ('4GB', '4GB'),
            ('8GB', '8GB'),
            ('16GB', '16GB'),
            ('32GB', '32GB'),
            ('64GB', '64GB'),
            ('128GB', '128GB'),
            ('256GB', '256GB'),
            ('512GB', '512GB'),
            ('1TB', '1TB'),
        ),
        )


class ChosenCpus(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    chosen_cpu = models.ForeignKey(
        to=AllCpus,
        on_delete=models.CASCADE,
        null=True,
    )
    build_custom_cpu = models.ForeignKey(
        to=CustomCpu,
        on_delete=models.CASCADE,
        null=True,
    )
    a = models.EmailField