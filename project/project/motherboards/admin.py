from django.contrib import admin

from project.motherboards.models import Motherboard


# Register your models here.
@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'manufacturer', 'model', 'form_factor', 'socket', 'user']
    search_fields = ['user__username']
