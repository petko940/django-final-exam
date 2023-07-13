from django.contrib import admin

from project.ram.models import RAM


# Register your models here.
@admin.register(RAM)
class ShowPCAdmin(admin.ModelAdmin):
    pass
