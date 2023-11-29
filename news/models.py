from django.db import models
from django.conf import settings

class News(models.Model):
    AUTOMATIC = 'AUTOMATIC'
    MANUAL = 'MANUAL'
    NEWS_TYPES = [
        (AUTOMATIC, 'Automatic'),
        (MANUAL, 'Manual'),
    ]

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст')
    news_type = models.CharField(max_length=10, choices=NEWS_TYPES, verbose_name='Тип новости')
    source = models.URLField(blank=True, null=True, verbose_name='Источник') # Used only if the news is automatic
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автор')  # Only set if the news is manual

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
