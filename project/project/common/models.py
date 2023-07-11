from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from project.cpus.models import ChosenCpus
from project.gpus.models import ChosenGpus
from project.motherboards.models import Motherboard
from project.ram.models import RAM
from project.storage.models import Storage

ModelUser = get_user_model()


class ShowPC(models.Model):
    user = models.ForeignKey(
        to=ModelUser,
        on_delete=models.CASCADE,
        editable=False,
    )
    choose_cpu = models.ForeignKey(
        to=ChosenCpus,
        on_delete=models.CASCADE
    )
    choose_gpu = models.ForeignKey(
        to=ChosenGpus,
        on_delete=models.CASCADE
    )
    choose_ram = models.ForeignKey(
        to=RAM,
        on_delete=models.CASCADE
    )
    choose_motherboards = models.ForeignKey(
        to=Motherboard,
        on_delete=models.CASCADE
    )
    choose_storage = models.ForeignKey(
        to=Storage,
        on_delete=models.CASCADE
    )
