from django.db import models

class Crypt(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    course = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Курс')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Криптаволюта'
        verbose_name_plural = 'Криптовалюта'