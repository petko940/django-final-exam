from django.contrib import admin
from .models import ChosenCpus


@admin.register(ChosenCpus)
class ChosenCpusAdmin(admin.ModelAdmin):
    list_display = ['user', 'chosen_cpu', 'build_custom_cpu']
