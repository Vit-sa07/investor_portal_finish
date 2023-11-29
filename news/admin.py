from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "news_type", "source", "created_by")
    search_fields = ("title", "content")
    ordering = ("-id",)  # Latest news first
