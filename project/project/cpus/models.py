from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
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
            MinValueValidator(1),
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
        max_length=30,
        validators=[
            MinLengthValidator(5, 'CPU name should be at least 5 characters long!'),
        ],
    )
    manufacturer = models.CharField(
        max_length=30
    )
    clock_speed = models.DecimalField(
        validators=[
            MinValueValidator(0.1, 'Clock speed should be bigger than 0!'),
        ],
        max_digits=4,
        decimal_places=2
    )
    number_of_cores = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, 'Choose cores between 1 and 512!'),
            MaxValueValidator(512, 'Choose cores between 1 and 512!'),
        ],
    )
    cache_size = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, 'Choose cache size between 1 and 1024(MB)!'),
            MaxValueValidator(1024, 'Choose cache size between 1 and 1024(MB)!')
        ],
    )
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
        verbose_name='Max RAM',
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
