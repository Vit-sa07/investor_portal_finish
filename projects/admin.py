from django.contrib import admin
from .models import Project, Investment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "payback", "airdrop_date", "token_unlock_date")
    search_fields = ("name", "description")
    ordering = ("name",)

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ("user", "project", "amount")
    search_fields = ("user__email", "project__name")
    ordering = ("-id",)
