from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AllGpus(models.Model):
    manufacturer = models.CharField(
        choices=(
            ('Nvidia', 'Nvidia'),
            ('AMD', 'AMD'),
            ('ATI', 'ATI'),
            ('Intel', 'Intel'),
        ),
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=25,
        blank=True,
        null=True
    )
    release_year = models.PositiveIntegerField(
        verbose_name='Release year',
        blank=True,
        null=True,
    )
    memory_size = models.FloatField(
        verbose_name='Memory size',
        blank=True,
        null=True,
    )
    memory_bus_width = models.PositiveIntegerField(
        verbose_name='Memory bus width',
        blank=True,
        null=True
    )
    gpu_clock = models.PositiveIntegerField(
        verbose_name='GPU clock',
        blank=True,
        null=True
    )
    memory_clock = models.PositiveIntegerField(
        verbose_name='Memory clock',
        blank=True,
        null=True
    )
    memory_type = models.CharField(
        verbose_name='Memory type',
        blank=True,
        null=True
    )


class ChosenGpus(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    chosen_gpu = models.ForeignKey(
        to=AllGpus,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.chosen_gpu.name} {self.chosen_gpu.memory_size}GB'
