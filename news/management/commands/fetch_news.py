from django.core.management.base import BaseCommand
from news.models import News

from .news_api import fetch_news_from_cryptocompare, translate_to_russian


# from news_api import fetch_news_from_cryptocompare, translate_to_russian


class Command(BaseCommand):
    help = 'Fetches, translates, and adds news to the database'

    def handle(self, *args, **kwargs):
        api_key = 'd9ced8ffbec2d31440c5f3a0d65ba35098f978938c3ba5d63f47e0abc2d2fd9e'
        news_items = fetch_news_from_cryptocompare(api_key)

        if news_items:
            for item in news_items:
                body = item['body']
                title = item['title']
                url = item['url']

                # Проверка на дублирование
                if not News.objects.filter(source=url).exists():
                    translated_body = translate_to_russian(body)
                    translated_title = translate_to_russian(title)

                    # Добавление в базу данных
                    News.objects.create(
                        title=translated_title,
                        content=translated_body,
                        news_type=News.AUTOMATIC,
                        source=url
                    )
                    self.stdout.write(self.style.SUCCESS(f'Added news item: {translated_title}'))