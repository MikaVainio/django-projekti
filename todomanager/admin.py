from django.contrib import admin

from .models import Tehtava



@admin.register(Tehtava)
class TehtavaAdmin(admin.ModelAdmin):
    fields = ["otsikko"]

