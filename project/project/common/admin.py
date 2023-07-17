from django.contrib import admin

from project.common.models import ShowPC


@admin.register(ShowPC)
class ShowPCAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'choose_cpu',
        'choose_gpu',
        'choose_ram',
        'choose_motherboards',
        'choose_storage'
    ]

    exclude = ['likes']
    list_filter = [
        'user',
        'choose_cpu',
        'choose_gpu',
        'choose_ram',
        'choose_motherboards',
        'choose_storage'
    ]
