from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

UserModel = get_user_model()


# Create your models here.
class Storage(models.Model):
    type = models.CharField(
        max_length=3,
        choices=(
            ('SSD', 'SSD'),
            ('HDD', 'HDD'),
        )
    )
    brand = models.CharField(
        max_length=20,
        choices=(
            ('Western Digital', 'Western Digital'),
            ('Seagate', 'Seagate'),
            ('Toshiba', 'Toshiba'),
            ('Samsung', 'Samsung'),
            ('Fujitsu', 'Fujitsu'),
            ('Kingston', 'Kingston'),
            ('Crucial', 'Crucial'),
            ('SanDisk', 'SanDisk'),
            ('ADATA', 'ADATA'),
            ('Corsair', 'Corsair'),
        )
    )
    capacity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(100, 'Capacity should be bigger than 100!')
        ],
        verbose_name='Capacity',
    )
    interface = models.CharField(
        choices=(
            ('SATA', 'SATA'),
            ('PCIe', 'PCIe'),
            ('NVMe', 'NVMe'),
            ('USB', 'USB'),
            ('Thunderbolt', 'Thunderbolt'),
        ),
        max_length=20
    )
    read_speed = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Read speed',
    )
    write_speed = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Write speed',
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        editable=False,
    )
