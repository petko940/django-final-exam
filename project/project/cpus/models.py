from django.contrib.auth.models import User
from django.db import models
from .validators import cpu_name_validator, cpu_clock_speed_validator, cpu_number_cores_validator, \
    cpu_cache_size_validator


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
    )
    threads = models.PositiveIntegerField(
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
    tdp = models.PositiveIntegerField(
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
            cpu_name_validator,
        ],
    )
    manufacturer = models.CharField(
        max_length=30
    )
    clock_speed = models.DecimalField(
        validators=[
            cpu_clock_speed_validator,
        ],
        max_digits=4,
        decimal_places=2
    )
    number_of_cores = models.PositiveIntegerField(
        validators=[
            cpu_number_cores_validator,
        ],
    )
    cache_size = models.PositiveIntegerField(
        validators=[
            cpu_cache_size_validator,
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
    )

    def save(self, *args, **kwargs):
        if not self.manufacturer[0].isdigit():
            self.manufacturer = self.manufacturer.capitalize()
        super().save(*args, **kwargs)


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

    def __str__(self):
        if self.chosen_cpu:
            output = f'{self.chosen_cpu.name} {self.chosen_cpu.cores}Cores {self.chosen_cpu.base_frequency}GHz'
            return output
        elif self.build_custom_cpu:
            output = f'{self.build_custom_cpu.name} {self.build_custom_cpu.number_of_cores}Cores {self.build_custom_cpu.clock_speed}GHz'
            return output
