from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Comments(models.Model):
    comment = models.TextField(verbose_name='Комментарий', max_length=500)
    author = models.ForeignKey(User, verbose_name='Автор комментария', on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents')
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now=True)


class Tasks(models.Model):
    name = models.CharField(verbose_name='Название задачи', max_length=50)
    description = models.TextField(verbose_name='Описание задачи', max_length=500)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    until_time = models.DateTimeField(verbose_name='Срок выполнения')
    author = models.ForeignKey(User, verbose_name='Постановщик', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, verbose_name='Ответственный', on_delete=models.CASCADE)
    watcher = models.ForeignKey(User, verbose_name='Наблюдатель', on_delete=models.CASCADE)
    STATUS = (
        (1, 'Новая задача'),
        (2, 'На выполнении'),
        (3, 'Выполнена')
    )
    status = models.IntegerField(verbose_name='Статус', choices=STATUS)
    file = models.FileField(upload_to='documents')
    comment = models.ManyToManyRel(Comments)
