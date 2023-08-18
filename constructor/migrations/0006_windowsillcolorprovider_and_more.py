# Generated by Django 4.1.2 on 2023-08-02 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0005_profiledoor_door_profile_door'),
    ]

    operations = [
        migrations.CreateModel(
            name='WindowsillColorProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название поставщика')),
                ('currency', models.CharField(blank=True, max_length=255, null=True, verbose_name='Валюта')),
            ],
            options={
                'verbose_name': 'Поставщик цветов подоконников',
                'verbose_name_plural': 'Поставщики цветов подоконников',
            },
        ),
        migrations.AddField(
            model_name='windowsillcolor',
            name='windowsill_provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.windowsillcolorprovider', verbose_name='Поставщик'),
        ),
    ]