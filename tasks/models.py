from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

STATUS_CHOISES = (
    ('Ожидает выполнения', 'Ожидает выполнения'),
    ('Выполняется', 'Выполняется'),
    ('Выполнена', 'Выполнена'),
    ('Отменена', 'Отменена'),
)


class Tasks(models.Model):
    name = models.CharField(_('Название задачи'), max_length=50)
    description = models.TextField(_('Описание задачи'), max_length=500)
    create_date = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    due_date = models.DateTimeField(_('Срок выполнения'))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    responsible = models.ForeignKey(User, related_name='responsible', on_delete=models.CASCADE)
    observer = models.ManyToManyField(User, related_name='observer', null=True)
    file = models.FileField(upload_to='documents', default=None)
    status = models.CharField(_('Статус'), max_length=20, choices=STATUS_CHOISES, default='Ожидает выполнения')


class Comments(models.Model):
    comment = models.TextField(_('Комментарий'), max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents', default=None)
    create_date = models.DateTimeField(_('Дата создания'), auto_now=True)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name="comments")



