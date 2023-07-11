from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from .validators import capacity_validator

UserModel = get_user_model()


# Create your models here.
class RAM(models.Model):
    DDR_CHOICES = (
        ('DDR1', 'DDR1'),
        ('DDR2', 'DDR2'),
        ('DDR3', 'DDR3'),
        ('DDR4', 'DDR4'),
        ('DDR5', 'DDR5'),
    )

    SPEED_CHOICES = {
        'DDR1': (
            ('200', '200 MHz'),
            ('266', '266 MHz'),
            ('333', '333 MHz'),
            ('400', '400 MHz'),
        ),
        'DDR2': (
            ('400', '400 MHz'),
            ('533', '533 MHz'),
            ('667', '667 MHz'),
            ('800', '800 MHz'),
            ('1000', '1000 MHz'),
        ),
        'DDR3': (
            ('800', '800 MHz'),
            ('1066', '1066 MHz'),
            ('1333', '1333 MHz'),
            ('1600', '1600 MHz'),
            ('1866', '1866 MHz'),
        ),
        'DDR4': (
            ('2133', '2133 MHz'),
            ('2400', '2400 MHz'),
            ('2666', '2666 MHz'),
            ('2933', '2933 MHz'),
            ('3200', '3200 MHz'),
            ('3600', '3600 MHz'),
        ),
        'DDR5': (
            ('3200', '3200 MHz'),
            ('3600', '3600 MHz'),
            ('4000', '4000 MHz'),
            ('4400', '4400 MHz'),
            ('4800', '4800 MHz'),
            ('5200', '5200 MHz'),
            ('5600', '5600 MHz'),
        )
    }
    SPEED = [
        ('200', '200 MHz'),
        ('266', '266 MHz'),
        ('333', '333 MHz'),
        ('400', '400 MHz'),
        ('533', '533 MHz'),
        ('667', '667 MHz'),
        ('800', '800 MHz'),
        ('1000', '1000 MHz'),
        ('1066', '1066 MHz'),
        ('1333', '1333 MHz'),
        ('1600', '1600 MHz'),
        ('1866', '1866 MHz'),
        ('2133', '2133 MHz'),
        ('2400', '2400 MHz'),
        ('2666', '2666 MHz'),
        ('2933', '2933 MHz'),
        ('3200', '3200 MHz'),
        ('3600', '3600 MHz'),
        ('4000', '4000 MHz'),
        ('4400', '4400 MHz'),
        ('4800', '4800 MHz'),
        ('5200', '5200 MHz'),
        ('5600', '5600 MHz'),
    ]
    brand = models.CharField(
        max_length=20,
        choices=(
            ('Corsair', 'Corsair'),
            ('Kingston', 'Kingston'),
            ('G.Skill', 'G.Skill'),
            ('Crucial', 'Crucial'),
            ('Samsung', 'Samsung'),
            ('ADATA', 'ADATA'),
            ('HyperX', 'HyperX'),
            ('Patriot', 'Patriot'),
            ('Silicon Power', 'Silicon Power'),
        )
    )
    memory_type = models.CharField(
        verbose_name='Memory type (DDR)',
        max_length=10,
        choices=DDR_CHOICES
    )
    speed = models.CharField(
        max_length=20,
        choices=SPEED,
    )
    capacity = models.PositiveIntegerField(
        verbose_name='Memory capacity (GB)',
        validators=[
            capacity_validator,
        ]
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        editable=False,
    )

    def __str__(self):
        return f'{self.brand} {self.capacity}GB {self.memory_type} {self.speed}MHz'