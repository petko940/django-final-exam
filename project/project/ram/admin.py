from django.contrib import admin

from project.ram.models import RAM


# Register your models here.
@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    list_display = ['user', 'brand', 'capacity', 'memory_type', 'speed']
