from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class TasksView(models.Model):
    name = models.CharField(verbose_name='Название задачи', max_length=50)
    description = models.TextField(verbose_name='Описание задачи', max_length=500)
    createdate = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    untiltime = models.DateTimeField(verbose_name='Выполнить до ')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, )
    recipient = models.ManyToManyField(User, related_name='Получатель', )
    STATUS = (
        (1, 'Новая задача'),
        (2, 'На выполнении'),
        (3, 'Выполнена')
    )
    status = models.IntegerField(verbose_name='Статус', choices=STATUS)