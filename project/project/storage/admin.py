from django.contrib import admin

from project.storage.models import Storage


# Register your models here.
@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'type',
        'brand',
        'display_capacity',
        'read_speed',
        'write_speed'
    ]
    search_fields = ['type']

    def display_capacity(self, obj):
        return f'{obj.capacity} GB'
