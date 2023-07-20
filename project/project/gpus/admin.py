from django.contrib import admin

from project.gpus.models import ChosenGpus


# Register your models here.
@admin.register(ChosenGpus)
class ChosenGpusAdmin(admin.ModelAdmin):
    list_display = ['user', 'chosen_gpu']
    search_fields = ['user__username']
