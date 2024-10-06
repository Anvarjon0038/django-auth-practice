from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    views = models.IntegerField('Просмотры', default=2)
    sizes = {
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('Xl', 'X large'),
    }

    shop_sizes = models.CharField('Размеры', max_length=2, choices=sizes, default='M')

    def __str__(self):
        return f'Новость: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'