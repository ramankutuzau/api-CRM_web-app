# Generated by Django 4.1.2 on 2023-07-24 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('constructor', '0002_rename_price_in_byn_lowtidesconnection_price_input_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0009_remove_client_passport_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalProfileCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('additional_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.additionalprofile', verbose_name='Доборный профиль')),
                ('lamination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.additionalprofilelamination', verbose_name='Ламинация профиль')),
            ],
            options={
                'verbose_name': 'Просчет доборного профиля',
                'verbose_name_plural': 'Просчеты доборных профилей',
            },
        ),
        migrations.CreateModel(
            name='CasingCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('casing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.casing', verbose_name='Наличник')),
                ('casing_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.casingcolor', verbose_name='Цвет наличника')),
            ],
            options={
                'verbose_name': 'Просчет наличника',
                'verbose_name_plural': 'Просчеты наличников',
            },
        ),
        migrations.CreateModel(
            name='ConnectionProfileCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('connection_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.connectionprofile', verbose_name='соединительный профиль')),
            ],
            options={
                'verbose_name': 'Просчет соединительного профиля',
                'verbose_name_plural': 'Просчеты соединительного профилей',
            },
        ),
        migrations.CreateModel(
            name='DoorCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип двери')),
                ('length', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота')),
                ('width', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ширина')),
                ('length_calc', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота просчета')),
                ('width_calc', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ширина просчета')),
                ('price_in_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена BYN')),
                ('filling', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.aggregate', verbose_name='Стеклопакет')),
                ('fittings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.fittings', verbose_name='Фурнитура')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Просчет двери',
                'verbose_name_plural': 'Просчеты дверей',
            },
        ),
        migrations.CreateModel(
            name='FlashingCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('flashing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.flashing', verbose_name='Нащельник')),
                ('flashing_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.flashingcolor', verbose_name='Цвет нащельника')),
            ],
            options={
                'verbose_name': 'Просчет нащельника',
                'verbose_name_plural': 'Просчеты нащельников',
            },
        ),
        migrations.CreateModel(
            name='InternalSlopesCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('internal_slopes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.internalslope', verbose_name='Внутренние откосы')),
                ('internal_slopes_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.internalslopecolor', verbose_name='Цвет внутреннего откоса')),
            ],
            options={
                'verbose_name': 'Просчет внутренних откосов',
                'verbose_name_plural': 'Просчеты внутренних откосов',
            },
        ),
        migrations.CreateModel(
            name='LowTidesCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('low_tides_width', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('low_tides_count', models.IntegerField(default=0, verbose_name='Количество  отливов')),
                ('low_tides_plug_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество заглушек')),
                ('low_tides_connection_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество соединителей')),
                ('square_meter', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='В метрах погонных')),
                ('sum_plug_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена заглушек в BYN')),
                ('sum_connection_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена соединитеей в BYN')),
                ('sum_low_tides_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена подоконника в BYN')),
                ('sum_in_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена BYN')),
                ('low_tides', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.lowtides', verbose_name='Отлив')),
                ('low_tides_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.lowtidescolor', verbose_name='Цвет отлива')),
                ('low_tides_connection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.lowtidesconnection', verbose_name='Соединитель отлива')),
                ('low_tides_plug', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.lowtidesplug', verbose_name='Заглушка отлива')),
            ],
            options={
                'verbose_name': 'Просчет отлива',
                'verbose_name_plural': 'Просчеты отливов',
            },
        ),
        migrations.CreateModel(
            name='MountingMaterialsCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('mounting_materials', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.mountingmaterials', verbose_name='Монтажные материалы')),
            ],
            options={
                'verbose_name': 'Просчет монтажных материалов',
                'verbose_name_plural': 'Просчеты внутренних монтажных материалов',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Единица измерия')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единица измерения',
            },
        ),
        migrations.CreateModel(
            name='WorksCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('works', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.works', verbose_name='Работа')),
            ],
            options={
                'verbose_name': 'Просчет работы',
                'verbose_name_plural': 'Просчеты работ',
            },
        ),
        migrations.CreateModel(
            name='WindowsillCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('windowsill_count', models.IntegerField(default=0, verbose_name='Количество  подоконников')),
                ('windowsill_plug_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество заглушек')),
                ('windowsill_connection_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество соединителей')),
                ('square_meter', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='В метрах погонных')),
                ('sum_plug_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена заглушек в BYN')),
                ('sum_connection_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена соединитеей в BYN')),
                ('sum_windowsill_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена подоконника в BYN')),
                ('sum_in_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена BYN')),
                ('windowsill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.windowsill', verbose_name='Подоконник')),
                ('windowsill_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.windowsillcolor', verbose_name='Цвет подоконника')),
                ('windowsill_connection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.windowsillconnection', verbose_name='Соединитель подоконника')),
                ('windowsill_plug', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.windowsillplug', verbose_name='Заглушка подоконника')),
                ('windowsill_width', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.windowsillwidth', verbose_name='Ширина подоконник')),
            ],
            options={
                'verbose_name': 'Просчет подоконника',
                'verbose_name_plural': 'Просчеты подоконников',
            },
        ),
        migrations.CreateModel(
            name='Windows4Calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('type_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип первой створки')),
                ('type_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип второй створки')),
                ('type_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип третей створки')),
                ('type_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип четвертой створки')),
                ('length', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота')),
                ('width', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ширина')),
                ('length_calc', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота просчета')),
                ('width_calc', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ширина просчета')),
                ('price_in_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена BYN')),
                ('filling', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.aggregate', verbose_name='Стеклопакет')),
                ('fittings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.fittings', verbose_name='Фурнитура')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Просчет 4-ст окна',
                'verbose_name_plural': 'Просчеты 4-ст окон',
            },
        ),
        migrations.CreateModel(
            name='Windows3Calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('type_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип первой створки')),
                ('type_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип второй створки')),
                ('type_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип третей створки')),
                ('length', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота')),
                ('width', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ширина')),
                ('length_calc', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота просчета')),
                ('width_calc', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ширина просчета')),
                ('price_in_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена BYN')),
                ('filling', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.aggregate', verbose_name='Стеклопакет')),
                ('fittings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.fittings', verbose_name='Фурнитура')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Просчет 3-ст окна',
                'verbose_name_plural': 'Просчеты 3-ст окон',
            },
        ),
        migrations.CreateModel(
            name='Windows2Calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('type_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип первой створки')),
                ('type_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип второй створки')),
                ('length', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота')),
                ('width', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ширина')),
                ('length_calc', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота просчета')),
                ('width_calc', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ширина просчета')),
                ('price_in_byn', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена BYN')),
                ('filling', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.aggregate', verbose_name='Стеклопакет')),
                ('fittings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.fittings', verbose_name='Фурнитура')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Просчет 2-ст окна',
                'verbose_name_plural': 'Просчеты 2-ст окон',
            },
        ),
        migrations.CreateModel(
            name='Windows1Calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип окна')),
                ('length', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота')),
                ('width', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ширина')),
                ('length_calc', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота просчета')),
                ('width_calc', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ширина просчета')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('filling', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.aggregate', verbose_name='Стеклопакет')),
                ('fittings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.fittings', verbose_name='Фурнитура')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Просчет 1-ст окна',
                'verbose_name_plural': 'Просчеты 1-ст окон',
            },
        ),
        migrations.CreateModel(
            name='VisorsCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('visors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.visors', verbose_name='Козырек')),
                ('visors_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.visorscolor', verbose_name='Цвет козырька')),
            ],
            options={
                'verbose_name': 'Просчет козырька',
                'verbose_name_plural': 'Просчеты козырьков',
            },
        ),
        migrations.CreateModel(
            name='SlopesOfMetalCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('slopes_of_metal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.slopesofmetal', verbose_name='Откосы из металла')),
                ('slopes_of_metal_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.slopesofmetalcolor', verbose_name='Цвет откоса из метлла')),
            ],
            options={
                'verbose_name': 'Просчет откосов из металла',
                'verbose_name_plural': 'Просчеты откосов из металла',
            },
        ),
        migrations.CreateModel(
            name='OtherCalcMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('price', models.FloatField(default=0, verbose_name='Цена')),
                ('other', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.othercomplectation', verbose_name='Работа')),
            ],
            options={
                'verbose_name': 'Просчет доп. расходов',
                'verbose_name_plural': 'Просчеты доп.расходов',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('room', models.CharField(blank=True, max_length=255, null=True, verbose_name='Комната')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата замера')),
                ('sum_materials_byn', models.FloatField(default=0.0, verbose_name='Сумма материалов в BYN')),
                ('sum_works_byn', models.FloatField(default=0.0, verbose_name='Сумма работ в BYN')),
                ('sum_other_byn', models.FloatField(default=0.0, verbose_name='Сумма доп. работ в BYN')),
                ('sum_windows_byn', models.FloatField(default=0.0, verbose_name='Сумма окон в BYN')),
                ('sum_byn', models.FloatField(default=0.0, verbose_name='Сумма просчета BYN')),
                ('additional_profile_calc', models.ManyToManyField(blank=True, to='measurer.additionalprofilecalcmob', verbose_name='Позиции доборных профилей')),
                ('casing_calc', models.ManyToManyField(blank=True, to='measurer.casingcalcmob', verbose_name='Позиции наличников')),
                ('connection_profile_calc', models.ManyToManyField(blank=True, to='measurer.connectionprofilecalcmob', verbose_name='Позиции соединительных профилей')),
                ('door_calc', models.ManyToManyField(blank=True, to='measurer.doorcalc', verbose_name='Позиции дверей')),
                ('flashing_calc', models.ManyToManyField(blank=True, to='measurer.flashingcalcmob', verbose_name='Позиции нащельников')),
                ('internal_slopes_calc', models.ManyToManyField(blank=True, to='measurer.internalslopescalcmob', verbose_name='Позиции внутренних откосов')),
                ('low_tides_calc', models.ManyToManyField(blank=True, to='measurer.lowtidescalcmob', verbose_name='Позиции отливов')),
                ('mounting_materials_calc', models.ManyToManyField(blank=True, to='measurer.mountingmaterialscalcmob', verbose_name='Позиции монтажных материалов')),
                ('other_calc', models.ManyToManyField(blank=True, to='measurer.othercalcmob', verbose_name='Позиции прочих расходов')),
                ('slopes_of_metal_calc', models.ManyToManyField(blank=True, to='measurer.slopesofmetalcalcmob', verbose_name='Позиции откосов из металла')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Замерщик')),
                ('visors_calc', models.ManyToManyField(blank=True, to='measurer.visorscalcmob', verbose_name='Позиции козырьков')),
                ('windows_1_calc', models.ManyToManyField(blank=True, to='measurer.windows1calc', verbose_name='Позиции 1-ст окон')),
                ('windows_2_calc', models.ManyToManyField(blank=True, to='measurer.windows2calc', verbose_name='Позиции 2-ст окон')),
                ('windows_3_calc', models.ManyToManyField(blank=True, to='measurer.windows3calc', verbose_name='Позиции 3-ст окон')),
                ('windows_4_calc', models.ManyToManyField(blank=True, to='measurer.windows4calc', verbose_name='Позиции 4-ст окон')),
                ('windowsill_calc', models.ManyToManyField(blank=True, to='measurer.windowsillcalcmob', verbose_name='Позиции подоконников')),
                ('works_calc', models.ManyToManyField(blank=True, to='measurer.workscalcmob', verbose_name='Позиции работ')),
            ],
            options={
                'verbose_name': 'Ордер',
                'verbose_name_plural': 'Ордер',
            },
        ),
        migrations.CreateModel(
            name='MiscalculationMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Населенный пункт')),
                ('area', models.CharField(blank=True, max_length=255, null=True, verbose_name='Район')),
                ('region', models.CharField(blank=True, max_length=255, null=True, verbose_name='Область')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Улица')),
                ('house', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дом')),
                ('floor', models.CharField(blank=True, max_length=255, null=True, verbose_name='Этаж')),
                ('flat', models.CharField(blank=True, max_length=255, null=True, verbose_name='Квартира')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата замера')),
                ('time', models.CharField(blank=True, max_length=255, null=True, verbose_name='Время замера')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя заказчика')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона')),
                ('status', models.CharField(blank=True, default='активный', max_length=255, null=True, verbose_name='статус')),
                ('total_cost', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Общая стоимость замера')),
                ('hidden_cost', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Скрытый расход')),
                ('manager_miscalculation', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Общая стоимость замера ( manager )')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client', verbose_name='Клиент')),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.contract', verbose_name='Договор')),
                ('orders', models.ManyToManyField(blank=True, to='measurer.order', verbose_name='Позиции')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Замерщик')),
            ],
            options={
                'verbose_name': 'Замер',
                'verbose_name_plural': 'Замеры',
            },
        ),
    ]
