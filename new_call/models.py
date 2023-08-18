from django.db import models


# Create your models here.

class OutgoingCalls(models.Model):
    phone = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.pk} {self.phone} {self.datetime} с телефона {self.number}'
