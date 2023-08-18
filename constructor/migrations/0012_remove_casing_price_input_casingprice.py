# Generated by Django 4.1.2 on 2023-08-13 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0011_windowsill_windowsill_connection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casing',
            name='price_input',
        ),
        migrations.CreateModel(
            name='CasingPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название наличника')),
                ('width_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='длинна от')),
                ('width_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='длинна до')),
                ('price_input', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Цена закупки')),
                ('casing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.casing', verbose_name='Наличник')),
                ('casing_provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.casingprovider', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Наличник',
                'verbose_name_plural': 'Наличники',
            },
        ),
    ]
