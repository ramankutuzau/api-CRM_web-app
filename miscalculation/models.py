from django.db import models

from calculation.models import Constructor


class Miscalculation(models.Model):
    author = models.CharField(max_length=255, blank=True,null=True)
    constructors = models.ManyToManyField(Constructor, verbose_name="Просчеты конструкторов", blank=True)
    created_time = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    last_update_time = models.DateTimeField(blank=True,null=True)
    sum = models.FloatField(max_length=255, default=0.0)
    status = models.CharField(max_length=255, blank=True,null=True)
    offer = models.BooleanField(max_length=255, blank=True,null=True)
    hidden_cost = models.FloatField(max_length=255, default=0.0, verbose_name='Скрытый расход', null=True,
                                   blank=True)
    def __str__(self):
        return f'Просчет №{self.id} на сумму {self.sum}'

    class Meta:
        verbose_name = 'Просчет полные'
        verbose_name_plural = 'Просчеты полные'


class CommercialOffer(models.Model):
    miscalculation = models.ForeignKey(Miscalculation, on_delete=models.SET_NULL, blank=True, null=True,
                                       verbose_name='Поставщик')
    image = models.FileField(upload_to='commercial_offers/', verbose_name='Ком. предложения',blank=True,null=True)

    class Meta:
        verbose_name = 'Коммерческое предложение'
        verbose_name_plural = 'Коммерческие предложения'