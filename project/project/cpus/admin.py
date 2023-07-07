from django.contrib import admin
from .models import AllCpus, CustomCpu, ChosenCpus


@admin.register(AllCpus)
class AllCpusAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomCpu)
class CustomCpuAdmin(admin.ModelAdmin):
    pass


@admin.register(ChosenCpus)
class ChosenCpusAdmin(admin.ModelAdmin):
    pass
