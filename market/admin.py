from django.contrib import admin
from .models import Crypt

@admin.register(Crypt)
class CryptAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "description")
    search_fields = ("name",)
    ordering = ("name",)
