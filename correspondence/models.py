from django.db import models


class IncomingMail(models.Model):
    name = models.CharField(max_length=255,blank=True)
    preview = models.FileField(upload_to='IncomingMail/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Входящая корреспонденция'
        verbose_name_plural = 'Входящая корреспонденция'


class OutgoingMail(models.Model):
    name = models.CharField(max_length=255,blank=True)
    preview = models.FileField(upload_to='OutgoingMail/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исходящая корреспонденция'
        verbose_name_plural = 'Исходящая корреспонденция'