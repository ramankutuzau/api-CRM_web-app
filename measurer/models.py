from django.db import models

from client.models import Client, Contract
from users.models import User
from constructor.models import *


# class ExchangeRates(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Имя')
#     value = models.FloatField(max_length=255, default=0.0, verbose_name='Значение')
#     auto = models.BooleanField(default=True, verbose_name='Получать автоматически')
#     add_percent = models.BooleanField(default=False, verbose_name='Добавлять в процентах')
#     value_percent = models.FloatField(max_length=255, default=0.0, verbose_name='Значение в процентах')
#
#     def __str__(self):
#         return f'1 {self.name} = {self.value} BYN '
#
#     class Meta:
#         verbose_name = 'Курс валют'
#         verbose_name_plural = 'Курсы валют'


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Unit(models.Model):
    name = models.CharField(max_length=100, verbose_name='Единица измерия', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единица измерения'


# class WindowsillPlug(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Заглушка подоконника'
#         verbose_name_plural = 'Заглушки подоконников'


# class WindowsillConnection(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Соединитель подоконника'
#         verbose_name_plural = 'Соединители подоконников'


class WindowsillCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    windowsill = models.ForeignKey(Windowsill, models.SET_NULL, verbose_name='Подоконник', blank=True, null=True)
    windowsill_width = models.ForeignKey(WindowsillWidth, models.SET_NULL, verbose_name='Ширина подоконник', blank=True,
                                         null=True)

    length = models.IntegerField(default=0, verbose_name='Длинна')
    windowsill_color = models.ForeignKey(WindowsillColor, models.SET_NULL, verbose_name='Цвет подоконника', blank=True,
                                         null=True)
    windowsill_count = models.IntegerField(default=0, verbose_name='Количество  подоконников')

    windowsill_plug = models.ForeignKey(WindowsillPlug, models.SET_NULL, verbose_name='Заглушка подоконника',
                                        blank=True,
                                        null=True)
    windowsill_plug_count = models.IntegerField(default=0, blank=True, null=True, verbose_name='Количество заглушек')
    windowsill_connection = models.ForeignKey(WindowsillConnection, models.SET_NULL,
                                              verbose_name='Соединитель подоконника', blank=True,
                                              null=True)
    windowsill_connection_count = models.IntegerField(default=0, blank=True, null=True,
                                                      verbose_name='Количество соединителей')

    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных', blank=True,
                                     null=True)
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных', blank=True,
                                     null=True)

    sum_plug_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена заглушек в BYN', blank=True,
                                     null=True)
    # sum_plug_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена заглушек в EUR/USD',
    #                                       blank=True, null=True)

    sum_connection_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена соединитеей в BYN',
                                           blank=True, null=True)
    # sum_connection_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена соединителей в EUR/USD',
    #                                             blank=True, null=True)

    sum_windowsill_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена подоконника в BYN',
                                           blank=True, null=True)
    # sum_windowsill_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена подоконника в EUR/USD',
    #                                             blank=True, null=True)

    sum_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN', blank=True, null=True)

    # sum_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD', blank=True, null=True)

    def __str__(self):
        return f' Номер замера {self.order_id} Подоконник {self.windowsill}  на сумму {self.sum_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет подоконника'
        verbose_name_plural = 'Просчеты подоконников'


# class LowTides(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#     unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Единица измерения')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Отлив'
#         verbose_name_plural = 'Отливы'


# class LowTidesType(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Тип Отлива'
#         verbose_name_plural = 'Типы отливов'


# class LowTidesPlug(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Заглушка отлива'
#         verbose_name_plural = 'Заглушки отливов'


# class LowTidesConnection(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Соединитель отлива'
#         verbose_name_plural = 'Соединители отливов'


# class LowTidesColor(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Цвет подоконника', blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Цвет отлива'
#         verbose_name_plural = 'Цвета отливов'


class LowTidesCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    low_tides = models.ForeignKey(LowTides, models.SET_NULL, verbose_name='Отлив', blank=True, null=True)
    low_tides_width = models.IntegerField(blank=True, null=True, default=0, verbose_name='Ширина')

    length = models.IntegerField(default=0, verbose_name='Длинна')
    low_tides_color = models.ForeignKey(LowTidesColor, models.SET_NULL, verbose_name='Цвет отлива', blank=True,
                                        null=True)
    # low_tides_type = models.ForeignKey(LowTidesType, models.SET_NULL, verbose_name='Тип отлива', blank=True,
    #                                    null=True)
    low_tides_count = models.IntegerField(default=0, verbose_name='Количество  отливов')

    low_tides_plug = models.ForeignKey(LowTidesPlug, models.SET_NULL, verbose_name='Заглушка отлива',
                                       blank=True,
                                       null=True)
    low_tides_plug_count = models.IntegerField(default=0, blank=True, null=True, verbose_name='Количество заглушек')
    low_tides_connection = models.ForeignKey(LowTidesConnection, models.SET_NULL,
                                             verbose_name='Соединитель отлива', blank=True,
                                             null=True)
    low_tides_connection_count = models.IntegerField(default=0, blank=True, null=True,
                                                     verbose_name='Количество соединителей')

    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных', blank=True,
                                     null=True)
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных', blank=True,
                                     null=True)

    sum_plug_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена заглушек в BYN', blank=True,
                                     null=True)
    # sum_plug_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена заглушек в EUR/USD',
    #                                       blank=True, null=True)

    sum_connection_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена соединитеей в BYN',
                                           blank=True, null=True)
    # sum_connection_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена соединителей в EUR/USD',
    #                                             blank=True, null=True)

    sum_low_tides_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена подоконника в BYN',
                                          blank=True, null=True)
    # sum_low_tides_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена подоконника в EUR/USD',
    #                                            blank=True, null=True)

    sum_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN', blank=True, null=True)

    # sum_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD', blank=True, null=True)

    def __str__(self):
        return f'{self.order_id}'

    class Meta:
        verbose_name = 'Просчет отлива'
        verbose_name_plural = 'Просчеты отливов'


# class VisorsColor(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Цвет козырька', blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Цвет козырька'
#         verbose_name_plural = 'Цвета козырьков'


# class Visors(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Козырек'
#         verbose_name_plural = 'козырьки'


class VisorsCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    visors = models.ForeignKey(Visors, models.SET_NULL, verbose_name='Козырек', blank=True, null=True)
    visors_color = models.ForeignKey(VisorsColor, models.SET_NULL, verbose_name='Цвет козырька', blank=True, null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина')
    width_1 = models.IntegerField(default=0, verbose_name='Ширина 1')
    width_2 = models.IntegerField(default=0, verbose_name='Ширина 2')
    width_3 = models.IntegerField(default=0, verbose_name='Ширина 3')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f'{self.order_id}'

    class Meta:
        verbose_name = 'Просчет козырька'
        verbose_name_plural = 'Просчеты козырьков'


# class AdditionalProfile(models.Model):
#     article = models.CharField(max_length=255, blank=True, null=True, verbose_name='Артикль')
#     width = models.FloatField(blank=True, null=True, verbose_name='Ширина')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.article} {self.width}'
#
#     class Meta:
#         verbose_name = 'Доборный профиль'
#         verbose_name_plural = 'Доборный профиль'


# class AdditionalProfileLamination(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ламинация')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Ламинация доборного профиль'
#         verbose_name_plural = 'Ламинация доборных профилей'


class AdditionalProfileCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    additional_profile = models.ForeignKey(AdditionalProfile, models.SET_NULL, verbose_name='Доборный профиль',
                                           blank=True, null=True)
    lamination = models.ForeignKey(AdditionalProfileLamination, models.SET_NULL, verbose_name='Ламинация профиль',
                                   blank=True, null=True)
    count = models.IntegerField(default=0, verbose_name='Количество')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} доборный профиль {self.additional_profile}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет доборного профиля'
        verbose_name_plural = 'Просчеты доборных профилей'


# class ConnectionProfile(models.Model):
#     article = models.CharField(max_length=255, blank=True, null=True, verbose_name='Артикль')
#     width = models.FloatField(blank=True, null=True, verbose_name='Ширина')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.article} {self.width}'
#
#     class Meta:
#         verbose_name = 'Соединительный профиль'
#         verbose_name_plural = 'Соединительный профиль'


class ConnectionProfileCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    connection_profile = models.ForeignKey(ConnectionProfile, models.SET_NULL, verbose_name='соединительный профиль',
                                           blank=True, null=True)

    count = models.IntegerField(default=0, verbose_name='Количество')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} соединительный профиль {self.connection_profile}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет соединительного профиля'
        verbose_name_plural = 'Просчеты соединительного профилей'


# class FlashingColor(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Цвет нащельника', blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Цвет нащельника'
#         verbose_name_plural = 'Цвета нащельников'


# class Flashing(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Нащельник'
#         verbose_name_plural = 'Нащельники'


class FlashingCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    flashing = models.ForeignKey(Flashing, models.SET_NULL, verbose_name='Нащельник', blank=True, null=True)
    flashing_color = models.ForeignKey(FlashingColor, models.SET_NULL, verbose_name='Цвет нащельника', blank=True,
                                       null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} Нащельник {self.flashing}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет нащельника'
        verbose_name_plural = 'Просчеты нащельников'


# class CasingColor(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Цвет наличника', blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Цвет наличника'
#         verbose_name_plural = 'Цвета наличников'


# class Casing(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Наличник'
#         verbose_name_plural = 'наличники'


class CasingCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    casing = models.ForeignKey(Casing, models.SET_NULL, verbose_name='Наличник', blank=True, null=True)
    casing_color = models.ForeignKey(CasingColor, models.SET_NULL, verbose_name='Цвет наличника', blank=True, null=True)

    width = models.IntegerField(default=0, verbose_name='Ширина')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} наличник {self.casing}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет наличника'
        verbose_name_plural = 'Просчеты наличников'


# class SlopesOfMetalColor(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Цвет откосов из металла', blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Цвет откоса из металла'
#         verbose_name_plural = 'Цвета откосов из металла'


# class SlopesOfMetal(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Откосы из металла'
#         verbose_name_plural = 'Откосы из металла'


class SlopesOfMetalCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    slopes_of_metal = models.ForeignKey(SlopesOfMetal, models.SET_NULL, verbose_name='Откосы из металла', blank=True,
                                        null=True)
    slopes_of_metal_color = models.ForeignKey(SlopesOfMetalColor, models.SET_NULL, verbose_name='Цвет откоса из метлла',
                                              blank=True, null=True)

    width = models.IntegerField(default=0, verbose_name='Ширина')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} Откос из металла {self.slopes_of_metal}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет откосов из металла'
        verbose_name_plural = 'Просчеты откосов из металла'


# class InternalSlopesColor(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Цвет внутренних откосов', blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Цвет внутренних откосов'
#         verbose_name_plural = 'Цвета внутренних откосов'
#
#
# class InternalSlopes(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Внутренние откосы'
#         verbose_name_plural = 'Внутренние откосы'


class InternalSlopesCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    internal_slopes = models.ForeignKey(InternalSlope, models.SET_NULL, verbose_name='Внутренние откосы', blank=True,
                                        null=True)
    internal_slopes_color = models.ForeignKey(InternalSlopeColor, models.SET_NULL,
                                              verbose_name='Цвет внутреннего откоса',
                                              blank=True, null=True)

    width = models.IntegerField(default=0, verbose_name='Ширина')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} внутренний откос {self.internal_slopes}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет внутренних откосов'
        verbose_name_plural = 'Просчеты внутренних откосов'


# class MountingMaterials(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Монтажные материалы'
#         verbose_name_plural = 'Монтажные материалы'


class MountingMaterialsCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    mounting_materials = models.ForeignKey(MountingMaterials, models.SET_NULL, verbose_name='Монтажные материалы',
                                           blank=True,
                                           null=True)
    count = models.IntegerField(default=0, verbose_name='Количество')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} монтажный материал {self.mounting_materials}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет монтажных материалов'
        verbose_name_plural = 'Просчеты внутренних монтажных материалов'


# class Works(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     # price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Работа'
#         verbose_name_plural = 'Работы'


# class Other(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
#     price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Дополнительные расходы'
#         verbose_name_plural = 'Дополнительные расходы'


class WorksCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    works = models.ForeignKey(Works, models.SET_NULL, verbose_name='Работа',
                              blank=True,
                              null=True)
    count = models.IntegerField(default=0, verbose_name='Количество')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} работа {self.works}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет работы'
        verbose_name_plural = 'Просчеты работ'


class OtherCalcMob(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    other = models.ForeignKey(OtherComplectation, models.SET_NULL, verbose_name='Работа',
                              blank=True,
                              null=True)
    price = models.FloatField(default=0, verbose_name='Цена')

    def __str__(self):
        return f' Номер замера {self.order_id} работа {self.other}  на сумму {self.price} BYN'

    class Meta:
        verbose_name = 'Просчет доп. расходов'
        verbose_name_plural = 'Просчеты доп.расходов'


# class Profile(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Профиль', blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Профиль'
#         verbose_name_plural = 'Профиля'
#
#
# class Fittings(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Фурнитура', blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Фурнитура'
#         verbose_name_plural = 'Фурнитуры'


# class Filling(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Стеклопакет', blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'Стеклопакет'
#         verbose_name_plural = 'Стеклопакеты'


class Windows1Calc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)

    profile = models.ForeignKey(Profile, verbose_name='Профиль', on_delete=models.SET_NULL, blank=True, null=True)
    fittings = models.ForeignKey(Fittings, verbose_name='Фурнитура', on_delete=models.SET_NULL, blank=True, null=True)
    filling = models.ForeignKey(Aggregate, verbose_name='Стеклопакет', on_delete=models.SET_NULL, blank=True, null=True)

    type = models.CharField(max_length=255, verbose_name='Тип окна', blank=True, null=True)
    length = models.IntegerField(default=0, verbose_name='Высота', blank=True, null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина', blank=True, null=True)
    length_calc = models.IntegerField(default=0, verbose_name='Высота просчета', blank=True, null=True)
    width_calc = models.IntegerField(default=0, verbose_name='Ширина просчета', blank=True, null=True)

    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f'{self.profile}'

    class Meta:
        verbose_name = 'Просчет 1-ст окна'
        verbose_name_plural = 'Просчеты 1-ст окон'


class Windows2Calc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)

    profile = models.ForeignKey(Profile, verbose_name='Профиль', on_delete=models.SET_NULL, blank=True, null=True)
    fittings = models.ForeignKey(Fittings, verbose_name='Фурнитура', on_delete=models.SET_NULL, blank=True, null=True)
    filling = models.ForeignKey(Aggregate, verbose_name='Стеклопакет', on_delete=models.SET_NULL, blank=True, null=True)

    type_1 = models.CharField(max_length=255, verbose_name='Тип первой створки', blank=True, null=True)
    type_2 = models.CharField(max_length=255, verbose_name='Тип второй створки', blank=True, null=True)
    length = models.IntegerField(default=0, verbose_name='Высота', blank=True, null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина', blank=True, null=True)
    length_calc = models.IntegerField(default=0, verbose_name='Высота просчета', blank=True, null=True)
    width_calc = models.IntegerField(default=0, verbose_name='Ширина просчета', blank=True, null=True)

    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN', null=True, blank=True)

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD', null=True,
    #                                       blank=True)

    def __str__(self):
        return f'{self.profile}'

    class Meta:
        verbose_name = 'Просчет 2-ст окна'
        verbose_name_plural = 'Просчеты 2-ст окон'


class Windows3Calc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)

    profile = models.ForeignKey(Profile, verbose_name='Профиль', on_delete=models.SET_NULL, blank=True, null=True)
    fittings = models.ForeignKey(Fittings, verbose_name='Фурнитура', on_delete=models.SET_NULL, blank=True, null=True)
    filling = models.ForeignKey(Aggregate, verbose_name='Стеклопакет', on_delete=models.SET_NULL, blank=True, null=True)

    type_1 = models.CharField(max_length=255, verbose_name='Тип первой створки', blank=True, null=True)
    type_2 = models.CharField(max_length=255, verbose_name='Тип второй створки', blank=True, null=True)
    type_3 = models.CharField(max_length=255, verbose_name='Тип третей створки', blank=True, null=True)
    length = models.IntegerField(default=0, verbose_name='Высота', blank=True, null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина', blank=True, null=True)
    length_calc = models.IntegerField(default=0, verbose_name='Высота просчета', blank=True, null=True)
    width_calc = models.IntegerField(default=0, verbose_name='Ширина просчета', blank=True, null=True)

    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN', null=True, blank=True)

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD', null=True,
    #                                       blank=True)

    def __str__(self):
        return f'{self.profile}'

    class Meta:
        verbose_name = 'Просчет 3-ст окна'
        verbose_name_plural = 'Просчеты 3-ст окон'


class Windows4Calc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)

    profile = models.ForeignKey(Profile, verbose_name='Профиль', on_delete=models.SET_NULL, blank=True, null=True)
    fittings = models.ForeignKey(Fittings, verbose_name='Фурнитура', on_delete=models.SET_NULL, blank=True, null=True)
    filling = models.ForeignKey(Aggregate, verbose_name='Стеклопакет', on_delete=models.SET_NULL, blank=True, null=True)

    type_1 = models.CharField(max_length=255, verbose_name='Тип первой створки', blank=True, null=True)
    type_2 = models.CharField(max_length=255, verbose_name='Тип второй створки', blank=True, null=True)
    type_3 = models.CharField(max_length=255, verbose_name='Тип третей створки', blank=True, null=True)
    type_4 = models.CharField(max_length=255, verbose_name='Тип четвертой створки', blank=True, null=True)
    length = models.IntegerField(default=0, verbose_name='Высота', blank=True, null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина', blank=True, null=True)
    length_calc = models.IntegerField(default=0, verbose_name='Высота просчета', blank=True, null=True)
    width_calc = models.IntegerField(default=0, verbose_name='Ширина просчета', blank=True, null=True)

    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN', null=True, blank=True)

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD', null=True,
    #                                       blank=True)

    def __str__(self):
        return f'{self.profile}'

    class Meta:
        verbose_name = 'Просчет 4-ст окна'
        verbose_name_plural = 'Просчеты 4-ст окон'


class DoorCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)

    profile = models.ForeignKey(Profile, verbose_name='Профиль', on_delete=models.SET_NULL, blank=True, null=True)
    fittings = models.ForeignKey(Fittings, verbose_name='Фурнитура', on_delete=models.SET_NULL, blank=True, null=True)
    filling = models.ForeignKey(Aggregate, verbose_name='Стеклопакет', on_delete=models.SET_NULL, blank=True, null=True)

    type = models.CharField(max_length=255, verbose_name='Тип двери', blank=True, null=True)
    length = models.IntegerField(default=0, verbose_name='Высота', blank=True, null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина', blank=True, null=True)
    length_calc = models.IntegerField(default=0, verbose_name='Высота просчета', blank=True, null=True)
    width_calc = models.IntegerField(default=0, verbose_name='Ширина просчета', blank=True, null=True)

    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN', null=True, blank=True)

    # price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD', null=True,
    #                                       blank=True)

    def __str__(self):
        return f'{self.profile}'

    class Meta:
        verbose_name = 'Просчет двери'
        verbose_name_plural = 'Просчеты дверей'


class Order(models.Model):
    active = models.BooleanField(default=True)
    room = models.CharField(max_length=255, verbose_name='Комната', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Замерщик')
    date = models.DateField(verbose_name='Дата замера', blank=True, null=True)
    sum_materials_byn = models.FloatField(default=0.0, verbose_name='Сумма материалов в BYN')
    sum_works_byn = models.FloatField(default=0.0, verbose_name='Сумма работ в BYN')
    sum_other_byn = models.FloatField(default=0.0, verbose_name='Сумма доп. работ в BYN')
    sum_windows_byn = models.FloatField(default=0.0, verbose_name='Сумма окон в BYN')
    sum_byn = models.FloatField(default=0.0, verbose_name='Сумма просчета BYN')

    windowsill_calc = models.ManyToManyField(WindowsillCalcMob, verbose_name='Позиции подоконников', blank=True)
    low_tides_calc = models.ManyToManyField(LowTidesCalcMob, verbose_name='Позиции отливов', blank=True)
    visors_calc = models.ManyToManyField(VisorsCalcMob, verbose_name='Позиции козырьков', blank=True)
    additional_profile_calc = models.ManyToManyField(AdditionalProfileCalcMob, verbose_name='Позиции доборных профилей',
                                                     blank=True)
    connection_profile_calc = models.ManyToManyField(ConnectionProfileCalcMob,
                                                     verbose_name='Позиции соединительных профилей', blank=True)
    flashing_calc = models.ManyToManyField(FlashingCalcMob, verbose_name='Позиции нащельников', blank=True)
    casing_calc = models.ManyToManyField(CasingCalcMob, verbose_name='Позиции наличников', blank=True)
    slopes_of_metal_calc = models.ManyToManyField(SlopesOfMetalCalcMob, verbose_name='Позиции откосов из металла',
                                                  blank=True)
    internal_slopes_calc = models.ManyToManyField(InternalSlopesCalcMob, verbose_name='Позиции внутренних откосов',
                                                  blank=True)
    mounting_materials_calc = models.ManyToManyField(MountingMaterialsCalcMob,
                                                     verbose_name='Позиции монтажных материалов', blank=True)
    works_calc = models.ManyToManyField(WorksCalcMob, verbose_name='Позиции работ', blank=True)
    other_calc = models.ManyToManyField(OtherCalcMob, verbose_name='Позиции прочих расходов', blank=True)
    windows_1_calc = models.ManyToManyField(Windows1Calc, verbose_name='Позиции 1-ст окон', blank=True)
    windows_2_calc = models.ManyToManyField(Windows2Calc, verbose_name='Позиции 2-ст окон', blank=True)
    windows_3_calc = models.ManyToManyField(Windows3Calc, verbose_name='Позиции 3-ст окон', blank=True)
    windows_4_calc = models.ManyToManyField(Windows4Calc, verbose_name='Позиции 4-ст окон', blank=True)
    door_calc = models.ManyToManyField(DoorCalc, verbose_name='Позиции дверей', blank=True)

    class Meta:
        verbose_name = 'Ордер'
        verbose_name_plural = 'Ордер'

    def __str__(self):
        return f' Active : {self.active} Сумма {self.sum_byn} BYN Сумма '


class MiscalculationMob(models.Model):
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Замерщик')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, verbose_name='Клиент')
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, verbose_name='Договор')
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name='Населенный пункт')
    area = models.CharField(max_length=255, blank=True, null=True, verbose_name='Район')
    region = models.CharField(max_length=255, blank=True, null=True, verbose_name='Область')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Улица')
    house = models.CharField(max_length=255, blank=True, null=True, verbose_name='Дом')
    floor = models.CharField(max_length=255, blank=True, null=True, verbose_name='Этаж')
    flat = models.CharField(max_length=255, blank=True, null=True, verbose_name='Квартира')
    date = models.DateField(verbose_name='Дата замера', blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True, verbose_name='Время замера')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя заказчика')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Номер телефона')
    status = models.CharField(max_length=255,verbose_name='статус', null=True, blank=True, default='активный')
    orders = models.ManyToManyField(Order, verbose_name='Позиции', blank=True)
    total_cost = models.FloatField(max_length=255, default=0.0, verbose_name='Общая стоимость замера', null=True,
                                   blank=True)
    hidden_cost = models.FloatField(max_length=255, default=0.0, verbose_name='Скрытый расход', null=True,
                                   blank=True)
    manager_miscalculation = models.FloatField(max_length=255, default=0.0, verbose_name='Общая стоимость замера ( manager )', null=True,
                                   blank=True)
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)

    class Meta:
        verbose_name = 'Замер'
        verbose_name_plural = 'Замеры'

    def __str__(self):
        return f' Адрес: {self.address} Cтатус: {self.status} общая стоимость {self.total_cost} BYN'
