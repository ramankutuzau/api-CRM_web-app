from django.db import models
from users.models import User


class Complaint(models.Model):
    author = models.CharField(max_length=255, verbose_name='Автор')
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Исполнитель', blank=True)
    content = models.CharField(max_length=255, verbose_name='Контент')
    status = models.CharField(max_length=255, verbose_name='Статус')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(verbose_name='Время обновления')
    time_deadline = models.DateTimeField(verbose_name='Срок задачи')
    overdue = models.BooleanField(default=False, verbose_name='Просрочена')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'