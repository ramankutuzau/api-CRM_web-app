# Generated by Django 4.1.2 on 2023-07-09 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calculation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miscalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update_time', models.DateTimeField(blank=True, null=True)),
                ('sum', models.FloatField(default=0.0, max_length=255)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('offer', models.BooleanField(blank=True, max_length=255, null=True)),
                ('constructors', models.ManyToManyField(blank=True, to='calculation.constructor', verbose_name='Просчеты конструкторов')),
            ],
            options={
                'verbose_name': 'Просчет полные',
                'verbose_name_plural': 'Просчеты полные',
            },
        ),
        migrations.CreateModel(
            name='CommercialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='commercial_offers/', verbose_name='Ком. предложения')),
                ('miscalculation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='miscalculation.miscalculation', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Коммерческое предложение',
                'verbose_name_plural': 'Коммерческие предложения',
            },
        ),
    ]