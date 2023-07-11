from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Motherboard(models.Model):
    MANUFACTURERS = (
        ('ASUS', 'ASUS'),
        ('GIGABYTE', 'GIGABYTE'),
        ('MSI', 'MSI'),
        ('ASRock', 'ASRock'),
        ('Intel', 'Intel'),
        ('Acer', 'Acer'),
        ('EVGA', 'EVGA'),
        ('Biostar', 'Biostar'),
        ('American Megatrends', 'American Megatrends'),
    )
    FORM_FACTORS = (
        ('Micro-ATX', 'Micro-ATX'),
        ('ATX', 'ATX'),
        ('Mini-ITX', 'Mini-ITX'),
        ('E-ATX', 'E-ATX'),
    )
    NETWORKING_CHOICES = (
        ('Ethernet', 'Ethernet'),
        ('Wi-Fi', 'Wi-Fi'),
        ('Ethernet/Wi-Fi', 'Ethernet/Wi-Fi'),
    )

    manufacturer = models.CharField(
        max_length=25,
        choices=MANUFACTURERS,
    )
    model = models.CharField(
        max_length=25,
    )
    form_factor = models.CharField(
        max_length=20,
        choices=FORM_FACTORS,
    )
    chipset = models.CharField(
        max_length=20,
    )
    socket = models.CharField(
        max_length=10
    )
    networking = models.CharField(
        max_length=20,
        choices=NETWORKING_CHOICES,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        editable=False,
    )

    def save(self, *args, **kwargs):
        self.chipset = ''.join([c.upper() if not c.isdigit() else c for c in self.chipset])
        self.socket = ''.join([c.upper() if not c.isdigit() else c for c in self.socket])

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.manufacturer} {self.model} {self.form_factor}'