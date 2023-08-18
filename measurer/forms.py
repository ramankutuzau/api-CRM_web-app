from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone

from client.models import PassportDetails
from .models import *
from constructor.models import *
from django.forms import ModelForm, TextInput, DateTimeInput, ChoiceField, ModelChoiceField, DateField, NumberInput, \
    BooleanField
from django import forms


class MySelect(forms.Select):
    def render_option(self, selected_choices, option_value, option_label):
        return u'<option whatever>...</option>'


class MiscalculationForm(ModelForm):
    date = forms.DateTimeField(
        label="Дата замера",
        required=True,
        widget=forms.NumberInput(attrs={'type': 'date', 'class': 'form-control mb-2'}),
        initial=timezone.now()  # Устанавливаем текущую дату и время как значение по умолчанию
    )

    class Meta:
        model = MiscalculationMob
        fields = ['phone', 'name', 'location', 'area', 'region', 'address', 'house', 'floor', 'flat', 'date', 'time']
        widgets = {
            'phone': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Номер телефона',
                'required': '',
            }),
            'name': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Имя клиента',
            }),

            'location': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Населенный пункт',
            }),
            'area': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Район',
            }),
            'region': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Область',
            }),
            'address': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Улица',
                'required': '',
            }),
            'house': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Дом',
            }),
            'flat': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Квартира',
            }),
            'floor': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Этаж',
            }),
            'time': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Время замера',
            }),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['room']
        widgets = {
            'room': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Помещение',
                'required': '',
            }),
        }
        #
        #     'name': TextInput(attrs={
        #         'class': 'form-control mb-2',
        #         'placeholder': 'Имя заказчика',
        #         'required': '',
        #     }),
        #     'phone': TextInput(attrs={
        #         'class': 'form-control mb-2',
        #         'placeholder': 'Номер телефона',
        #         'required': '',
        #     }),
        #
        # }


class WindowsillCalcForm(ModelForm):
    windowsill = ModelChoiceField(
        queryset=Windowsill.objects.all(), empty_label="Выберите подоконник", label='Подоконник',
        widget=MySelect(attrs={
            'id': 'windowsill-select',
            'class': 'form-control mb-2',
            'placeholder': 'Подоконник',
        }), required=False, blank=True
    )

    windowsill_width = ModelChoiceField(
        queryset=WindowsillWidth.objects.all(), empty_label="Выберите ширину подоконника", label='Полка подоконник',
        widget=MySelect(attrs={
            'name': 'Ширина подоконник',
            'class': 'form-control mb-2',
            'placeholder': 'Полка подоконник',
        }), required=False, blank=True
    )

    windowsill_color = ModelChoiceField(
        queryset=WindowsillColor.objects.all(), empty_label="Выберите цвет подоконника", label='Цвет подоконник',
        widget=MySelect(attrs={
            'name': 'Цвет подоконника',
            'class': 'form-control mb-2',
            'placeholder': 'Цвета подоконник',
        }), required=False, blank=True
    )

    windowsill_plug = ModelChoiceField(
        queryset=WindowsillPlug.objects.all(), empty_label="Выберите заглушку", label='Заглушка',
        widget=MySelect(attrs={
            'id': 'windowsill-plug-select',
            'class': 'form-control mb-2',
            'placeholder': 'Заглушка',
        }), required=False, blank=True
    )

    windowsill_connection = ModelChoiceField(
        queryset=WindowsillConnection.objects.all(), empty_label="Выберите соединитель", label='Соединитель',
        widget=MySelect(attrs={
            'name': 'Соединитель',
            'class': 'form-control mb-2',
            'placeholder': 'Соединитель',
        }), required=False, blank=True
    )

    class Meta:
        model = WindowsillCalcMob
        fields = ['windowsill_width', 'length', 'windowsill', 'windowsill_count', 'windowsill_color', 'windowsill_plug',
                  'windowsill_plug_count', 'windowsill_connection', 'windowsill_connection_count']
        widgets = {
            'windowsill_plug_count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество 6'
            }),
            'windowsill_connection_count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество соединителей'
            }),
            'length': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Длина'
            }),
            'windowsill_count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество подоконников'
            }),

        }


class LowTidesCalcForm(ModelForm):
    low_tides = ModelChoiceField(
        queryset=LowTides.objects.all(), empty_label="Выберите отлив", label='Отлив',
        widget=MySelect(attrs={
            'name': 'Отлив',
            'id': 'low-tides-select',
            'class': 'form-control mb-2',
            'placeholder': 'Отлив',
        }), required=False, blank=True
    )

    low_tides_type = ModelChoiceField(
        queryset=LowTidesType.objects.all(), empty_label="Выберите тип отлива", label='Тип Отлив',
        widget=MySelect(attrs={
            'name': 'Тип Отлив',
            'class': 'form-control mb-2',
            'placeholder': 'Тип отлив',
        }), required=False, blank=True
    )
    low_tides_color = ModelChoiceField(
        queryset=LowTidesColor.objects.all(), empty_label="Выберите цвет отлива", label='Цвет Отлива',
        widget=MySelect(attrs={
            'name': 'Цвет отлива',
            'class': 'form-control mb-2',
            'placeholder': 'Цвета отлива',
        }), required=False, blank=True
    )

    low_tides_plug = ModelChoiceField(
        queryset=LowTidesPlug.objects.all(), empty_label="Выберите заглушку", label='Заглушка',
        widget=MySelect(attrs={
            'name': 'Заглушка',
            'id': 'low-tides-plug-select',
            'class': 'form-control mb-2',
            'placeholder': 'Заглушка',
        }), required=False, blank=True
    )

    low_tides_connection = ModelChoiceField(
        queryset=LowTidesConnection.objects.all(), empty_label="Выберите соединитель", label='Соединитель',
        widget=MySelect(attrs={
            'name': 'Соединитель',
            'class': 'form-control mb-2',
            'placeholder': 'Соединитель',
        }), required=False, blank=True
    )

    class Meta:
        model = LowTidesCalcMob
        fields = ['low_tides_width', 'length', 'low_tides', 'low_tides_type', 'low_tides_color', 'low_tides_count',
                  'low_tides_plug',
                  'low_tides_plug_count', 'low_tides_connection', 'low_tides_connection_count']
        widgets = {
            'low_tides_width': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Ширина'
            }),
            'low_tides_plug_count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество '
            }),
            'low_tides_connection_count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество соединителей'
            }),
            'length': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Длина'
            }),
            'low_tides_count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество отливов',
            }),

        }


class AdditionalProfileCalcForm(ModelForm):
    additional_profile = ModelChoiceField(
        queryset=AdditionalProfile.objects.all(), empty_label="Выберите доборный профиль",
        label='Доборный профиль',
        widget=MySelect(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Доборный профиль',
        }), required=True, blank=True
    )
    lamination = ModelChoiceField(
        queryset=AdditionalProfileLamination.objects.all(), empty_label="Выберите Ламинацию",
        label='Доборный профиль',
        widget=MySelect(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ламинация доборного профиля',
        }), required=False, blank=True
    )

    class Meta:
        model = AdditionalProfileCalcMob
        fields = ['additional_profile', 'lamination', 'count']
        widgets = {
            'count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество доборных профилей'
            }),

        }


class ConnectionProfileCalcForm(ModelForm):
    connection_profile = ModelChoiceField(
        queryset=ConnectionProfile.objects.all(), empty_label="Выберите Cоединительный профиль",
        label='Cоединительный профиль',
        widget=MySelect(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Доборный профиль',
        }), required=True, blank=True
    )

    class Meta:
        model = ConnectionProfileCalcMob
        fields = ['connection_profile', 'count']
        widgets = {
            'lamination_2': BooleanField(required=False),
            'count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество соединительных профилей'
            }),

        }


class VisorsCalcForm(ModelForm):
    visors = ModelChoiceField(
        queryset=Visors.objects.all(), empty_label="Выберите козырек", label='Козырек',
        widget=MySelect(attrs={
            'name': 'Козырек',
            'class': 'form-control mb-2',
            'placeholder': 'Козырек',
        })
    )
    visors_color = ModelChoiceField(
        queryset=VisorsColor.objects.all(), empty_label="Выберите цвет козырька", label='Цвет Козырька',
        widget=MySelect(attrs={
            'name': 'Цвет козырька',
            'class': 'form-control mb-2',
            'placeholder': 'Цвета козырьков',
        })
    )
    width_1 = forms.FloatField(
        label='Ширина А',
        widget=forms.NumberInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ширина А',


        })
    )

    width_2 = forms.FloatField(
        label='Ширина Б',
        widget=forms.NumberInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ширина Б',

        })
    )

    width_3 = forms.FloatField(
        label='Ширина В',
        widget=forms.NumberInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ширина В',


        })
    )
    class Meta:
        model = VisorsCalcMob
        fields = ['visors', 'visors_color', 'width_1','width_2','width_3', 'length', 'count']
        widgets = {
            'length': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Длина'
            }),

            'count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }


class FlashingCalcForm(ModelForm):
    flashing = ModelChoiceField(
        queryset=Flashing.objects.all(), empty_label="Выберите нащельник", label='Нащельник',
        widget=MySelect(attrs={
            'name': 'Нащельник',
            'class': 'form-control mb-2',
            'placeholder': 'Нащельник',
        })
    )
    flashing_color = ModelChoiceField(
        queryset=FlashingColor.objects.all(), empty_label="Выберите цвет нащельника", label='Цвет Нащельника',
        widget=MySelect(attrs={
            'name': 'Цвет нащельника',
            'class': 'form-control mb-2',
            'placeholder': 'Цвета нащельников',
        })
    )

    class Meta:
        model = VisorsCalcMob
        fields = ['flashing', 'flashing_color', 'width', 'length', 'count']
        widgets = {
            'length': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Длина'
            }),
            'width': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Ширина'
            }),
            'count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }


class CasingCalcForm(ModelForm):
    casing = ModelChoiceField(
        queryset=Casing.objects.all(), empty_label="Выберите наличник", label='Наличники',
        widget=MySelect(attrs={
            'name': 'Наличники',
            'class': 'form-control mb-2',
            'placeholder': 'Наличники',
        })
    )
    casing_color = ModelChoiceField(
        queryset=CasingColor.objects.all(), empty_label="Выберите цвет наличника", label='Цвет наличника',
        widget=MySelect(attrs={
            'name': 'Цвет наличника',
            'class': 'form-control mb-2',
            'placeholder': 'Цвета наличников',
        })
    )

    class Meta:
        model = CasingCalcMob
        fields = ['casing', 'casing_color', 'width', 'length', 'count']
        widgets = {
            'length': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Длина'
            }),
            'width': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Ширина'
            }),
            'count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }


class SlopesOfMetalCalcForm(ModelForm):
    slopes_of_metal = ModelChoiceField(
        queryset=SlopesOfMetal.objects.all(), empty_label="Выберите откос из металла", label='Откос из металла',
        widget=MySelect(attrs={
            'name': 'Откос из металла',
            'class': 'form-control mb-2',
            'placeholder': 'Откос из металла',
        })
    )
    slopes_of_metal_color = ModelChoiceField(
        queryset=SlopesOfMetalColor.objects.all(), empty_label="Выберите цвет откоса из металла",
        label='Цвет откоса из металла',
        widget=MySelect(attrs={
            'name': 'Цвет откоса из металла',
            'class': 'form-control mb-2',
            'placeholder': 'Цвета откосов из металла',
        })
    )

    class Meta:
        model = SlopesOfMetalCalcMob
        fields = ['slopes_of_metal', 'slopes_of_metal_color', 'width', 'length', 'count']
        widgets = {
            'length': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Длина'
            }),
            'width': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Ширина'
            }),
            'count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }


class InternalSlopesCalcForm(ModelForm):
    internal_slopes = ModelChoiceField(
        queryset=InternalSlope.objects.all(), empty_label="Выберите откосы", label='Откосы',
        widget=MySelect(attrs={
            'name': 'Откосы',
            'class': 'form-control mb-2',
            'placeholder': 'откосы',
        })
    )
    internal_slopes_color = ModelChoiceField(
        queryset=InternalSlopeColor.objects.all(), empty_label="Выберите цвет внутреннего откоса",
        label='Цвет внутреннего откоса',
        widget=MySelect(attrs={
            'name': 'Цвет внутреннего откоса',
            'class': 'form-control mb-2',
            'placeholder': 'Цвета внутреннего откоса',
        })
    )

    class Meta:
        model = InternalSlopesCalcMob
        fields = ['internal_slopes', 'internal_slopes_color', 'width', 'length', 'count']
        widgets = {
            'length': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Длина'
            }),
            'width': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Ширина'
            }),
            'count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }


class MountingMaterialsCalcForm(ModelForm):
    mounting_materials = ModelChoiceField(
        queryset=MountingMaterials.objects.all(), empty_label="Выберите монтажные материалы",
        label='Монтажные материалы',
        widget=MySelect(attrs={
            'name': 'Монтажые материалы',
            'class': 'form-control mb-2',
            'placeholder': 'Монтажные материалы',
        })
    )

    class Meta:
        model = MountingMaterialsCalcMob
        fields = ['mounting_materials', 'count']
        widgets = {
            'count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }


class WorksCalcForm(ModelForm):
    works = ModelChoiceField(
        queryset=Works.objects.all(), empty_label="Выберите работу",
        label='Работы',
        widget=MySelect(attrs={
            'name': 'Работы',
            'class': 'form-control mb-2',
            'placeholder': 'Работы',
        })
    )

    class Meta:
        model = WorksCalcMob
        fields = ['works', 'count']
        widgets = {
            'count': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Количество'
            }),

        }


class OtherCalcForm(ModelForm):
    other = ModelChoiceField(
        queryset=OtherComplectation.objects.all(), empty_label="Выберите наименование",
        label='Наименование',
        widget=MySelect(attrs={
            'name': 'Работы',
            'class': 'form-control mb-2',
            'placeholder': 'Работы',
        })
    )

    class Meta:
        model = OtherCalcMob
        fields = ['other', 'price']
        widgets = {
            'price': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Цена'
            }),

        }


class PassportDetailsForm(ModelForm):
    class Meta:
        model = PassportDetails
        fields = ['name', 'series_number',  'personal_number', 'issued_by', 'address', 'email',]
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'ФИО',
                'required': '',
            }),
            'series_number': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Серия и номер ',
                'required': '',
            }),

            'personal_number': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Личный номер',
                'required': '',
            }),
            'issued_by': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Кем выдан',
                'required': '',
            }),
            'address': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Адрес прописки',
                'required': '',
            }),
            'email': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'email',
            }),
        }

class ContractForm(ModelForm):

    class Meta:
        model = Contract
        fields = ['delivery_address', 'deposit',]
        widgets = {

            'delivery_address': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Адрес доставки ',
                'required': '',
            }),
            'deposit': NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Задаток',
            }),

        }