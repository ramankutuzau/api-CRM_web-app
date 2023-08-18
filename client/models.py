from django.db import models

from call.models import CallWindow
from miscalculation.models import Miscalculation
from complaint.models import Complaint
from calculation.models import Constructor


class Prompter(models.Model):
    category_select = models.IntegerField(blank=True, null=True, verbose_name="Категория выбора")
    main_statements = models.CharField(max_length=255, blank=True, verbose_name="Основные высказывания")
    type_home = models.CharField(max_length=255, blank=True, null=True, verbose_name="Тип дома")
    built_from_other = models.CharField(max_length=255, blank=True, null=True, verbose_name="Из чего построен")
    sun_heating = models.BooleanField(default=False, blank=True, verbose_name='Летом солнце нагревает')
    weak_light = models.BooleanField(default=False, blank=True, verbose_name='Мало света ')
    noise_outside = models.BooleanField(default=False, blank=True, verbose_name='Шум за окном')
    winter_cold = models.CharField(max_length=255, default=False, blank=True, verbose_name='Зимой холодно')
    rose_of_wind = models.BooleanField(default=False, blank=True, verbose_name='Роза ветров')
    children = models.BooleanField(default=False, blank=True, verbose_name='Есть ли дети')
    installation_room = models.CharField(max_length=255, blank=True, null=True, verbose_name="Комната установки")
    special_offers = models.CharField(max_length=255, blank=True, verbose_name='Специальные предложения')
    solution_window = models.CharField(max_length=255, blank=True, verbose_name='Почему решили поменять окно')
    only_window = models.BooleanField(default=False, blank=True, verbose_name='Только окно')
    mounting_all = models.CharField(max_length=255, blank=True, null=True, verbose_name="Монтаж отливов/подоконников")
    slopes = models.BooleanField(default=False, blank=True, verbose_name='Отделка откосов')
    mosquito_net = models.BooleanField(default=False, blank=True, verbose_name='Москитная сетка')
    room = models.CharField(max_length=255, blank=True, verbose_name='В какую комнату установка')
    individual_wishes = models.CharField(max_length=255, blank=True, verbose_name='Индивидуальные пожелания')
    floor = models.CharField(max_length=255, default=False, blank=True, verbose_name='Комнаты')
    layout = models.CharField(max_length=255, default=False, blank=True, verbose_name='')
    reason_window_change = models.CharField(max_length=255, default=False, blank=True, verbose_name='')
    address = models.CharField(max_length=255, default=False, blank=True, verbose_name='')

    def __str__(self):
        return self.main_statements


class Number(models.Model):
    number = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.number} {self.name}'


class Address(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class PassportDetails(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='ФИО')
    series_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='Серия и номер')
    personal_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='Личный номер')
    issued_by = models.CharField(max_length=255, blank=True, null=True, verbose_name='Кем выдан')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Прописка')
    email = models.CharField(max_length=255, blank=True, null=True)


class Contract(models.Model):
    number = models.CharField(max_length=255,blank=True,null=True, verbose_name='Номер договора')
    passport_details = models.ForeignKey(PassportDetails, models.SET_NULL, blank=True,null=True, verbose_name='Паспортные данные')
    date = models.DateField(blank=True,null=True, verbose_name='Дата договора')
    delivery_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адресс доставки')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Номер телефона')
    cost = models.FloatField(max_length=255,blank=True,null=True, verbose_name='Стоимость')
    deposit = models.FloatField(max_length=255,blank=True,null=True, verbose_name='Задаток')
    finish_cost = models.FloatField(max_length=255,blank=True,null=True, verbose_name='Окончательная стоимость')
    signed = models.BooleanField(default=False, verbose_name='Подписан')


class Client(models.Model):
    author = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    numbers = models.ManyToManyField(Number, blank=True)
    addresses = models.ManyToManyField(Address, blank=True)
    prompter = models.ManyToManyField(Prompter, blank=True)
    passport_details = models.ForeignKey(PassportDetails,on_delete=models.SET_NULL, blank=True, null=True)
    contract = models.ManyToManyField(Contract, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    calls = models.ManyToManyField(CallWindow, blank=True)
    miscalculation = models.ManyToManyField(Miscalculation, verbose_name="Просчеты конструкторов", blank=True)
    complaints = models.ManyToManyField(Complaint, verbose_name="Жалобы", blank=True)

    def __str__(self):
        return f' {self.name} {self.numbers}'
