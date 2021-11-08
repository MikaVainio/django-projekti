from django.contrib import admin

from .models import Kategoria, Tehtava


@admin.register(Tehtava)
class TehtavaAdmin(admin.ModelAdmin):
    pass


@admin.register(Kategoria)
class KategoriaAdmin(admin.ModelAdmin):
    pass
