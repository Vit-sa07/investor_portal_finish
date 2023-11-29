from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "surname", "balance", "invested")
    search_fields = ("email", "name", "surname")
    ordering = ("email",)
