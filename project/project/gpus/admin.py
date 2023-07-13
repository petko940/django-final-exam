from django.contrib import admin

from project.gpus.models import ChosenGpus


# Register your models here.
@admin.register(ChosenGpus)
class AllGpusAdmin(admin.ModelAdmin):
    pass
