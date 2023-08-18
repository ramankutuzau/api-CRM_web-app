from django.db import models


class CallOkna(models.Model):
    id_call = models.CharField(max_length=255, blank=True, null=True)


class CallWindow(models.Model):
    id_call = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    call_status = models.CharField(max_length=255, blank=True, null=True)
    call_type = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.datetime} {self.number}'
