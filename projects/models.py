from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    logo = models.ImageField(upload_to='projects/logos/', verbose_name='Логотип')
    payback = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Окупаемость')
    website_url = models.URLField(verbose_name='Ссылка на сайт проекта')
    contract_url = models.URLField(verbose_name='Ссылка на контракт в блокчейне')
    detailed_description_url = models.URLField(verbose_name='Ссылка на подробное описание')
    airdrop_date = models.DateField(verbose_name='Дата AirDrop')
    token_unlock_date = models.DateField(verbose_name='Дата разблокировки токенов')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Investment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')

    def __str__(self):
        return f"{self.user.email} - {self.project.name}"


    class Meta:
        verbose_name = 'Инвестиция'
        verbose_name_plural = 'Инвестиции'
