from django.db import models
from django.forms import TextInput


class ProviderWindow(models.Model):
    name = models.CharField(max_length=255, verbose_name="Поставщик", blank=True, null=True)
    currency = models.CharField(max_length=255, verbose_name="Валюта", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик профиля'
        verbose_name_plural = 'Поставщики профилей'


# _______________________________ CONFIGURATION MODEL _______________________________
class ProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Тип изделия", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип изделия'
        verbose_name_plural = 'Тип изделия'


class Profile(models.Model):
    TYPE = [(0, 'Прямой'),
            (1, 'Фигурный')]
    name = models.CharField(max_length=255, verbose_name="Профиль", blank=True, null=True)
    type = models.PositiveSmallIntegerField(('type'), choices=TYPE, blank=True, null=True)

    provider_profile = models.ForeignKey(ProviderWindow, on_delete=models.SET_NULL, blank=True, null=True,
                                         verbose_name='Поставщик')

    def __str__(self):
        return f'№ {self.pk} имя : {self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиля'


class ProfileDoor(models.Model):
    TYPE = [(0, 'Прямой'),
            (1, 'Фигурный')]
    name = models.CharField(max_length=255, verbose_name="Профиль", blank=True, null=True)
    type = models.PositiveSmallIntegerField(('type'), choices=TYPE, blank=True, null=True)

    provider_profile = models.ForeignKey(ProviderWindow, on_delete=models.SET_NULL, blank=True, null=True,
                                         verbose_name='Поставщик')

    def __str__(self):
        return f'№ {self.pk} имя : {self.name}'

    class Meta:
        verbose_name = 'Профиль дверной'
        verbose_name_plural = 'Профиля дверные'


class ProductTypeDoor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Тип изделия", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип изделия двери'
        verbose_name_plural = 'Тип изделия двери'


class Opening(models.Model):
    name = models.CharField(max_length=255, verbose_name="Открывание", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Открывание'
        verbose_name_plural = 'Открывания'


class Lock(models.Model):
    name = models.CharField(max_length=255, verbose_name="Дверной замок", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дверной замок'
        verbose_name_plural = 'Дверные замки'


class DoorHandles(models.Model):
    name = models.CharField(max_length=255, verbose_name="Дверная ручки", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дверная ручка'
        verbose_name_plural = 'Дверные ручки'


class DoorHinges(models.Model):
    name = models.CharField(max_length=255, verbose_name="Дверные петли", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дверные петли'
        verbose_name_plural = 'Дверные петли'


class Cylinder(models.Model):
    name = models.CharField(max_length=255, verbose_name="Цилиндр", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цилиндр'
        verbose_name_plural = 'Цилиндры'


class DoorCloser(models.Model):
    name = models.CharField(max_length=255, verbose_name="Доводчик", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доводчик'
        verbose_name_plural = 'Доводчики'


class OpeningLimiter(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ограничитель открывания", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ограничитель открывания'
        verbose_name_plural = 'Ограничители открывания'


class Door(models.Model):
    product_type = models.ForeignKey(ProductTypeDoor, on_delete=models.SET_NULL, verbose_name="Тип изделия", blank=True,
                                     null=True)
    profile_door = models.ForeignKey(ProfileDoor, on_delete=models.SET_NULL, verbose_name="Дверной профиль", blank=True,
                                     null=True)
    shtulp = models.BooleanField(default=False, verbose_name='Со штульпом', blank=True)
    opening = models.ForeignKey(Opening, on_delete=models.SET_NULL, verbose_name="Открывание", blank=True, null=True)
    lock = models.ForeignKey(Lock, on_delete=models.SET_NULL, verbose_name="Замок", blank=True, null=True)
    handle = models.ForeignKey(DoorHandles, on_delete=models.SET_NULL, verbose_name="Дверные ручки", blank=True,
                               null=True)
    door_hinges = models.ForeignKey(DoorHinges, on_delete=models.SET_NULL, verbose_name="Дверные петли", blank=True,
                                    null=True)
    cylinder = models.ForeignKey(Cylinder, on_delete=models.SET_NULL, verbose_name="Цилиндр", blank=True, null=True)
    door_closer = models.ForeignKey(DoorCloser, on_delete=models.SET_NULL, verbose_name="Доводчик", blank=True,
                                    null=True)
    opening_limiter = models.ForeignKey(OpeningLimiter, on_delete=models.SET_NULL,
                                        verbose_name="Ограничитель открывания", blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk} {self.product_type}'

    class Meta:
        verbose_name = 'Дверь'
        verbose_name_plural = 'Двери'


class Article(models.Model):
    name = models.CharField(max_length=255, verbose_name="Артикуль", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Артикуль'
        verbose_name_plural = 'Артикули'


class ConnectionProfileName(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название соед.профиля", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название соед.профиля'
        verbose_name_plural = 'Название соед.профиля'


class ColorInside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Цвет внутри", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет внутри'
        verbose_name_plural = 'Цвета внутри'


class ColorOutside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Цвет снаружи", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет снаружи'
        verbose_name_plural = 'Цвета снаружи'


class ConnectionProfile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Профиль", blank=True, null=True)
    connection_article = models.ForeignKey(Article, on_delete=models.SET_NULL, verbose_name="Артикуль", blank=True,
                                           null=True)
    name = models.ForeignKey(ConnectionProfileName, on_delete=models.SET_NULL, verbose_name="Название соен.профиля",
                             blank=True, null=True)
    color_inside = models.ForeignKey(ColorInside, on_delete=models.SET_NULL, verbose_name="Цвет внутри", blank=True,
                                     null=True)
    color_outside = models.ForeignKey(ColorOutside, on_delete=models.SET_NULL, verbose_name="Цвет снаружи", blank=True,
                                      null=True)
    length = models.FloatField(default=0.0, verbose_name="Длина", blank=True, null=True)
    price = models.FloatField(default=0.0, verbose_name="Цена", blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk} {self.name}'

    class Meta:
        verbose_name = 'Соединительные профиля'
        verbose_name_plural = 'Соединительные профиля'


class ArticleAdditionalProfile(models.Model):
    name = models.CharField(max_length=255, verbose_name="Артикуль", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Артикуль доб. профиля'
        verbose_name_plural = 'Артикуль доб. профиля'


class AdditionalProfileLamination(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ламинация')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Ламинация доборного профиль'
        verbose_name_plural = 'Ламинация доборных профилей'


class AdditionalProfile(models.Model):
    additional_article = models.ForeignKey(ArticleAdditionalProfile, on_delete=models.SET_NULL, verbose_name="Артикуль",
                                           blank=True, null=True)
    width = models.FloatField(default=0.0, verbose_name="Ширина", blank=True, null=True)
    price = models.FloatField(default=0.0, verbose_name="Цена", blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk} {self.additional_article}'

    class Meta:
        verbose_name = 'Доборный профиль'
        verbose_name_plural = 'Доборные профиля'


class SealantColor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Цвет уплотнения", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет уплотнения'
        verbose_name_plural = 'Цвет уплотнения'


class SealantOutside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Исполнение снаружи", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнение снаружи уплотнителя'
        verbose_name_plural = 'Исполнение снаружи уплотнителя'


class SealantInside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Исполнение внутри", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнение внутри уплотнителя'
        verbose_name_plural = 'Исполнение внутрии уплотнителя'


class SealantShtapik(models.Model):
    name = models.CharField(max_length=255, verbose_name="Уплотнитель", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = f'Уплотнитель ( штапик )'
        verbose_name_plural = f'Уплотнитель ( штапики ) '


class Sealant(models.Model):
    sealant_color = models.ForeignKey(SealantColor, on_delete=models.SET_NULL, verbose_name="Цвет уплотнителя",
                                      blank=True, null=True)
    sealant_inside = models.ForeignKey(SealantInside, on_delete=models.SET_NULL, verbose_name="Исполнение снаружи",
                                       blank=True, null=True)
    sealant_outside = models.ForeignKey(SealantOutside, on_delete=models.SET_NULL, verbose_name="Исполнение внутри",
                                        blank=True, null=True)
    sealant_shtapik = models.ForeignKey(SealantShtapik, on_delete=models.SET_NULL, verbose_name="Штапик",
                                        blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk}'

    class Meta:
        verbose_name = 'Уплотнитель'
        verbose_name_plural = 'Уплотнители'


class TypeLamination(models.Model):
    name = models.CharField(max_length=255, verbose_name="Тип ламинации", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип ламинации'
        verbose_name_plural = 'Типы ламинации'


class TypeLamination2(models.Model):
    name = models.CharField(max_length=255, verbose_name="Вид ламинации", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид ламинации'
        verbose_name_plural = 'Виды ламинации'


class SealInternal(models.Model):
    name = models.CharField(max_length=255, verbose_name="Исполнение внутри", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнение внутри'
        verbose_name_plural = 'Исполнение внутри'


class SealOutside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Исполнение снаружи", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнение снаружи'
        verbose_name_plural = 'Исполнение снаружи'


class SealBasic(models.Model):
    name = models.CharField(max_length=255, verbose_name="Исполнение основы детали", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнение основы детали'
        verbose_name_plural = 'Исполнение основы детали'


class Lamination(models.Model):
    type_lamination = models.ForeignKey(TypeLamination, on_delete=models.SET_NULL, verbose_name="Тип ламинации",
                                        blank=True, null=True)
    type_lamination1 = models.ForeignKey(TypeLamination2, on_delete=models.SET_NULL, verbose_name="Вид ламинации",
                                         blank=True, null=True)
    seal_internal = models.ForeignKey(SealInternal, on_delete=models.SET_NULL, verbose_name="Исполнение внутри",
                                      blank=True, null=True)
    seal_outside = models.ForeignKey(SealOutside, on_delete=models.SET_NULL, verbose_name="Исполнение снаружи",
                                     blank=True, null=True)
    seal_basic = models.ForeignKey(SealBasic, on_delete=models.SET_NULL, verbose_name="Исполнение основы детали",
                                   blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk} {self.type_lamination.name}'

    class Meta:
        verbose_name = 'Ламинация'
        verbose_name_plural = 'Ламинации'


# class Sealant(models.Model):
#     color = models.CharField(max_length=255, verbose_name="Цвет", blank=True, null=True)
#     execution_outside = models.CharField(max_length=255, verbose_name="Исполнение снаружи", blank=True, null=True)
#     execution_inside = models.CharField(max_length=255, verbose_name="Исполнение внутри", blank=True, null=True)
#     shtapik = models.CharField(max_length=255, verbose_name="Штапик", blank=True, null=True)
#
#     def __str__(self):
#         return self.color
#
#     class Meta:
#         verbose_name = 'Уплотнитель'
#         verbose_name_plural = 'Уплотнители'


class Shtapik(models.Model):
    name = models.CharField(max_length=255, verbose_name="Штапик", blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk} имя : {self.name}'

    class Meta:
        verbose_name = 'Штапик'
        verbose_name_plural = 'Штапики'


class Fittings(models.Model):
    name = models.CharField(max_length=255, verbose_name="Фурнитура", blank=True, null=True)

    # price = models.FloatField(verbose_name="Цена", blank=True, null=True)
    # discount = models.FloatField(verbose_name="Скидка", blank=True, null=True)

    def __str__(self):
        return f'№ {self.id} имя : {self.name}'

    class Meta:
        verbose_name = 'Фурнитура'
        verbose_name_plural = 'Фурнитуры'


class Aggregate(models.Model):
    CAMERA_CHOICES = (
        (1, '1-ух камерный'),
        (2, '2-ух камерный'),
    )
    RAMKA_CHOICE = (
        (1, 'Стандарт'),
        (2, 'Черная'),
        (3, 'Белая'),
    )
    TYPE_CHOICE = (
        (1, 'Sendwich'),
        (2, 'Энергосберегающие'),
        (3, 'EnergyAir'),
        (4, 'Тонированные'),
        (5, 'Фениксы'),
        (6, 'Феникс клер'),
        (7, 'Феникс бронза'),
        (8, 'Феникс грей'),
        (9, 'CRYSTALVISION'),
        (10, 'Антирезонансные'),
        (11, 'Антивандальные'),
        (12, 'Триплекс'),
        (13, 'Простые'),
    )
    name = models.CharField(max_length=255, verbose_name="Заполнитель №1", blank=True, null=True)
    article = models.CharField(max_length=255, verbose_name="Артикул", blank=True, null=True)
    camera = models.IntegerField(choices=CAMERA_CHOICES, verbose_name="Камера", default=1)
    ramka = models.IntegerField(choices=RAMKA_CHOICE, verbose_name="Рамка", default=1)
    type = models.IntegerField(choices=TYPE_CHOICE, verbose_name="Тип", default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заполнитель №1'
        verbose_name_plural = 'Заполнитель №1'


# class SealOutside(models.Model):
#     name = models.CharField(max_length=255, verbose_name="Уплотнение снаружи", blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Уплотнение снаружи'
#         verbose_name_plural = 'Уплотнение снаружи'


class SealRebate(models.Model):
    name = models.CharField(max_length=255, verbose_name="Уплотнение притвора", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уплотнение притвора'
        verbose_name_plural = 'Уплотнение притвора'


# class SealInternal(models.Model):
#     name = models.CharField(max_length=255, verbose_name="Уплотнение внутренее", blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Уплотнение внутренее'
#         verbose_name_plural = 'Уплотнение внутренее'


class Shpros(models.Model):
    name = models.CharField(max_length=255, verbose_name="Шпрос", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Шпрос'
        verbose_name_plural = 'Шпросы'


# class Shtapik(models.Model):
#     name = models.CharField(max_length=255, verbose_name="Штапик", blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Штапик'
#         verbose_name_plural = 'Штапики'


class Sash(models.Model):
    name = models.CharField(max_length=255, verbose_name="Створка", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Створка'
        verbose_name_plural = 'Створки'


class Gorbylki(models.Model):
    name = models.CharField(max_length=255, verbose_name="Горбыльки", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Горбыльки'
        verbose_name_plural = 'Горбыльки'


class LaminationOutside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ламинация снаружи", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ламинация снаружи'
        verbose_name_plural = 'Ламинация снаружи'


class LaminationInside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ланиманция внутри", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ланиманция внутри'
        verbose_name_plural = 'Ланиманция внутри'


class ProfileWeight(models.Model):
    name = models.CharField(max_length=255, verbose_name="Масса профиля", blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.name}'

    class Meta:
        verbose_name = 'Масса профиля'
        verbose_name_plural = 'Масса профиля'


class Note(models.Model):
    name = models.CharField(max_length=255, verbose_name="Примечание", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Примечание'
        verbose_name_plural = 'Примечание'


# _______________________________ EXTRAWORK MODEL _______________________________


class ProductsInstall(models.Model):
    name = models.CharField(max_length=255, verbose_name="Монтаж изделий", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Монтаж изделий'
        verbose_name_plural = 'Монтаж изделий'


class PvcSlopes(models.Model):
    name = models.CharField(max_length=255, verbose_name="Откосы ПВХ", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Откосы ПВХ'
        verbose_name_plural = 'Откосы ПВХ'


class FreePositions(models.Model):
    name = models.CharField(max_length=255, verbose_name="Бесплатные позиции", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бесплатные позиции'
        verbose_name_plural = 'Бесплатные позиции'


# _______________________________ EXTRAMATERIAL MODEL _______________________________
class WindowsillInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    price = models.FloatField(default=0.0, verbose_name='Цена монтажа', blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена монтажа: {self.price}'

    class Meta:
        verbose_name = 'Монтаж подоконника'
        verbose_name_plural = 'Монтажи подоконников'

class WindowsillColorProvider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название поставщика", blank=True, null=True)
    currency = models.CharField(max_length=255, verbose_name="Валюта", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Поставщик цветов подоконников'
        verbose_name_plural = 'Поставщики цветов подоконников'



class WindowsillWidth(models.Model):
    name = models.CharField(max_length=100, verbose_name='Полка подоконника', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Полка подоконника'
        verbose_name_plural = 'Полки подоконников'


class WindowsillProvider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название поставщика", blank=True, null=True)
    currency = models.CharField(max_length=255, verbose_name="Валюта", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Поставщик подоконников'
        verbose_name_plural = 'Поставщики подоконников'

class WindowsillColor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название цвета", blank=True, null=True)
    windowsill_provider = models.ForeignKey(WindowsillProvider, blank=True, on_delete=models.SET_NULL, null=True,
                                            verbose_name='Поставщик')
    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Цвет подоконника'
        verbose_name_plural = 'Цвета подоконников'
class WindowsillPlug(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    # price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
    price_input = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
    windowsill_plug_provider = models.ForeignKey(WindowsillProvider, blank=True, on_delete=models.SET_NULL, null=True,
                                            verbose_name='Поставщик')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Заглушка подоконника'
        verbose_name_plural = 'Заглушки подоконников'





class WindowsillConnection(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    # price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
    price_input = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Соединитель подоконника'
        verbose_name_plural = 'Соединители подоконников'


class Windowsill(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название подоконника", blank=True, null=True)
    type = models.CharField(max_length=255, verbose_name='Тип подоконника', blank=True, null=True)
    price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)
    windowsill_provider = models.ForeignKey(WindowsillProvider, blank=True, on_delete=models.SET_NULL, null=True,
                                            verbose_name='Поставщик')
    windowsill_plug = models.ForeignKey(WindowsillPlug, blank=True, on_delete=models.SET_NULL, null=True,  related_name='plug_windowsills',
                                            verbose_name='Заглушка')
    windowsill_connection = models.ForeignKey(WindowsillConnection, blank=True, on_delete=models.SET_NULL, null=True,related_name='connection_windowsills',
                                            verbose_name='Соединитель')

    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Подоконник'
        verbose_name_plural = 'Подоконники'
class LowTidesInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    price = models.FloatField(default=0.0, verbose_name='Цена монтажа', blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена монтажа: {self.price}'

    class Meta:
        verbose_name = 'Монтаж отлива'
        verbose_name_plural = 'Монтажи отливов'


class LowTidesPlug(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    # price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
    price_input = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Заглушка отлива'
        verbose_name_plural = 'Заглушки отливов'


class LowTidesConnection(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    # price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
    price_input = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Соединитель отлива'
        verbose_name_plural = 'Соединители отливов'





class LowTidesType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип Отлива'
        verbose_name_plural = 'Типы отливов'


class LowTidesProvider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название поставщика", blank=True, null=True)
    currency = models.CharField(max_length=255, verbose_name="Валюта", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Поставщик отливов'
        verbose_name_plural = 'Поставщики отливов'

class LowTidesColor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название цвета", blank=True, null=True)
    low_tides_provider = models.ForeignKey(LowTidesProvider, blank=True, on_delete=models.SET_NULL, null=True,
                                            verbose_name='Поставщик')
    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Цвет отлива'
        verbose_name_plural = 'Цвета отливов'

class LowTides(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название отлива", blank=True, null=True)

    price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)
    low_tides_provider = models.ForeignKey(LowTidesProvider, blank=True, on_delete=models.SET_NULL, null=True,
                                           verbose_name='Поставщик')

    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Отлив'
        verbose_name_plural = 'Отливы'


class FlashingInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    price = models.FloatField(default=0.0, verbose_name='Цена монтажа', blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена монтажа: {self.price}'

    class Meta:
        verbose_name = 'Монтаж нащельника'
        verbose_name_plural = 'Монтажи нащельников'




class FlashingProvider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название поставщика", blank=True, null=True)
    currency = models.CharField(max_length=255, verbose_name="Валюта", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Поставщик нащельников'
        verbose_name_plural = 'Поставщики нащельников'

class FlashingColor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название цвета", blank=True, null=True)
    flashing_provider = models.ForeignKey(FlashingProvider, blank=True, on_delete=models.SET_NULL, null=True,
                                           verbose_name='Поставщик')
    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Цвет нащельника'
        verbose_name_plural = 'Цвета нащельников'



class Flashing(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название нащельника')
    price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)
    flashing_provider = models.ForeignKey(FlashingProvider, blank=True, on_delete=models.SET_NULL, null=True,
                                          verbose_name='Поставщик')
    TYPE = [(0, 'Металл'),
            (1, 'Пластик')]
    width = models.FloatField(default=0.0, verbose_name='Ширина', blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Профиль", blank=True, null=True)
    type = models.PositiveSmallIntegerField(('type'), choices=TYPE, blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Нащельник'
        verbose_name_plural = 'Нащельники'


class CasingFastening(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название крепление", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name}'

    class Meta:
        verbose_name = 'Крепление наличника'
        verbose_name_plural = 'Крепления наличников'


class CasingInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    price = models.FloatField(default=0.0, verbose_name='Цена монтажа', blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена монтажа: {self.price}'

    class Meta:
        verbose_name = 'Монтаж наличника'
        verbose_name_plural = 'Монтажи наличников'




class CasingProvider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название поставщика", blank=True, null=True)
    currency = models.CharField(max_length=255, verbose_name="Валюта", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Поставщик наличников'
        verbose_name_plural = 'Поставщики наличников'

class CasingColor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название цвета", blank=True, null=True)
    casing_provider = models.ForeignKey(CasingProvider, blank=True, on_delete=models.SET_NULL, null=True,
                                          verbose_name='Поставщик')
    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Цвет наличника'
        verbose_name_plural = 'Цвета наличников'



class Casing(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название наличника')
    # price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)
    casing_provider = models.ForeignKey(CasingProvider, on_delete=models.SET_NULL, blank=True, null=True,
                                        verbose_name='Поставщик')

    def __str__(self):
        return f'# {self.pk} Название: {self.name}'

    class Meta:
        verbose_name = 'Наличник'
        verbose_name_plural = 'Наличники'

class CasingNipelPrice(models.Model):
    casing = models.ForeignKey(Casing, on_delete=models.SET_NULL, blank=True, null=True,
                                        verbose_name='Наличник')
    price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)
    casing_provider = models.ForeignKey(CasingProvider, on_delete=models.SET_NULL, blank=True, null=True,
                                        verbose_name='Поставщик')

    def __str__(self):
        return f'# {self.pk} цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Нипели для наличников'
        verbose_name_plural = 'Нипели для наличников '
class CasingPrice(models.Model):
    casing = models.ForeignKey(Casing, on_delete=models.SET_NULL, blank=True, null=True,
                                        verbose_name='Наличник')
    width = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ширина')

    price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)
    casing_provider = models.ForeignKey(CasingProvider, on_delete=models.SET_NULL, blank=True, null=True,
                                        verbose_name='Поставщик')

    def __str__(self):
        return f'# {self.pk} Название: {self.casing.name}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Наличник цены'
        verbose_name_plural = 'Наличники цены'

class VisorsInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    price = models.FloatField(default=0.0, verbose_name='Цена монтажа', blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена монтажа: {self.price}'

    class Meta:
        verbose_name = 'Монтаж козырька'
        verbose_name_plural = 'Монтажи козырьков'





class VisorsProvider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название поставщика", blank=True, null=True)
    currency = models.CharField(max_length=255, verbose_name="Валюта", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Поставщик козырьков'
        verbose_name_plural = 'Поставщики козырьков'

class VisorsColor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название цвета", blank=True, null=True)
    visors_provider = models.ForeignKey(VisorsProvider, blank=True, on_delete=models.SET_NULL, null=True,
                                          verbose_name='Поставщик')
    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Цвет козырька'
        verbose_name_plural = 'Цвета козырьков'

class Visors(models.Model):
    name = models.CharField(max_length=255, verbose_name='Развертка козырька', blank=True, null=True)
    price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)
    visors_provider = models.ForeignKey(VisorsProvider, on_delete=models.SET_NULL, blank=True, null=True,
                                        verbose_name='Поставщик')

    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Козырек'
        verbose_name_plural = 'Козырьки'





class SlopesOfMetalColor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название цвета", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Цвет откосов из металла'
        verbose_name_plural = 'Цвета откосов из металла'


class SlopesOfMetalProvider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название поставщика", blank=True, null=True)
    currency = models.CharField(max_length=255, verbose_name="Валюта", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Поставщик откосов из металла'
        verbose_name_plural = 'Поставщики откосов из металла'

class SlopesOfMetalInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    price = models.FloatField(default=0.0, verbose_name='Цена монтажа', blank=True, null=True)
    slopes_of_metal_provider = models.ForeignKey(SlopesOfMetalProvider, blank=True, on_delete=models.SET_NULL, null=True,
                                          verbose_name='Поставщик')
    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена монтажа: {self.price}'

    class Meta:
        verbose_name = 'Монтаж откосов из металла'
        verbose_name_plural = 'Монтажи откосов из металла'

class SlopesOfMetal(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Тип откосов из металла')
    price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)
    slopes_of_metal_provider = models.ForeignKey(SlopesOfMetalProvider, on_delete=models.SET_NULL, blank=True,
                                                 null=True, verbose_name='Поставщик')

    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Откосы из металла'
        verbose_name_plural = 'откосы из металла'





class InternalSlopeColor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название цвета", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Цвет внутренних откосов'
        verbose_name_plural = 'Цвета внутренних откосов'


class InternalSlopeProvider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название поставщика", blank=True, null=True)
    currency = models.CharField(max_length=255, verbose_name="Валюта", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Поставщик внутренние откосы'
        verbose_name_plural = 'Поставщики внутренние откосы'

class InternalSlopeInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    price = models.FloatField(default=0.0, verbose_name='Цена монтажа', blank=True, null=True)
    internal_provider = models.ForeignKey(InternalSlopeProvider, blank=True, on_delete=models.SET_NULL,
                                                 null=True,
                                                 verbose_name='Поставщик')
    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена монтажа: {self.price}'

    class Meta:
        verbose_name = 'Монтаж внутренних откосов'
        verbose_name_plural = 'Монтажи внутренних откосов'

class InternalSlope(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True, verbose_name='Тип внутренних откосов')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Наименование внутренних откосов')
    price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)
    internal_slope_provider = models.ForeignKey(InternalSlopeProvider, on_delete=models.SET_NULL, blank=True, null=True,
                                                verbose_name='Поставщик')

    def __str__(self):
        return f'# {self.pk} Название: {self.name}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Внутренние откосы'
        verbose_name_plural = 'Внутренние откосы'


class MountingMaterialsName(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Наименование монтажных материалов')

    def __str__(self):
        return f'# {self.pk} Название: {self.name}'

    class Meta:
        verbose_name = 'Монтажные материалы'
        verbose_name_plural = 'Монтажные материалы'


class MountingMaterials(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    # price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
    price_input = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Монтажные материалы'
        verbose_name_plural = 'Монтажные материалы'


class MountingMaterialsProvider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название поставщика", blank=True, null=True)
    currency = models.CharField(max_length=255, verbose_name="Валюта", blank=True, null=True)

    def __str__(self):
        return f'# {self.pk} Название: {self.name} '

    class Meta:
        verbose_name = 'Поставщик материалов'
        verbose_name_plural = 'Поставщики материалов'


class MountingMaterialsType(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True, verbose_name='Тип монтажных материалов')

    price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)
    mounting_materials_provider = models.ForeignKey(MountingMaterialsProvider, on_delete=models.SET_NULL, blank=True,
                                                    null=True, verbose_name='Поставщик')

    def __str__(self):
        return f'# {self.pk} Название: {self.type}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Тип монтажного материала'
        verbose_name_plural = 'Типы монтажных материалов'


class Handles(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ручка", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ручка'
        verbose_name_plural = 'Ручки'


class OtherComplectation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Прочее комплектующие", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прочее комплектующие'
        verbose_name_plural = 'Прочее комплектующие'


class Works(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование работы', blank=True, null=True)
    price = models.FloatField(max_length=255, default=0.0, verbose_name='Цена работы')

    def __str__(self):
        return f' Работы № {self.pk} {self.name} на сумму {self.price} BYN'

    class Meta:
        verbose_name = 'Работы'
        verbose_name_plural = 'Работы'
