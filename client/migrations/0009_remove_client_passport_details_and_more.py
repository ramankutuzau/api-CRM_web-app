# Generated by Django 4.1.2 on 2023-07-24 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_contract_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='passport_details',
        ),
        migrations.AddField(
            model_name='client',
            name='passport_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.passportdetails'),
        ),
    ]