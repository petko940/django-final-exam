from django.contrib import admin

from project.common.models import ShowPC


@admin.register(ShowPC)
class AllCpusAdmin(admin.ModelAdmin):
    pass
