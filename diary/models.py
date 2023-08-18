from django.db import models
from users.models import User
from client.models import Client


class TypeTask(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    author = models.CharField(max_length=255, verbose_name='Автор')
    type_task_id = models.ForeignKey(TypeTask, on_delete=models.SET_NULL, null=True, verbose_name='Тип задачи',blank=True)
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Исполнитель',blank=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, verbose_name='Клиент',blank=True)
    content = models.CharField(max_length=255, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now_add=True, verbose_name='Время обновления')
    time_deadline = models.DateTimeField(verbose_name='Срок задачи')
    overdue = models.BooleanField(default=False, verbose_name='Просрочена')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return self.content


