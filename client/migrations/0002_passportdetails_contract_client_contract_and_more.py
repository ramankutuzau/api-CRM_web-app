# Generated by Django 4.1.2 on 2023-07-23 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassportDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('series', models.CharField(blank=True, max_length=255, null=True)),
                ('personal_number', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('issued_by', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('delivery_address', models.CharField(blank=True, max_length=255, null=True)),
                ('cost', models.FloatField(blank=True, max_length=255, null=True)),
                ('deposit', models.FloatField(blank=True, max_length=255, null=True)),
                ('finish_cost', models.FloatField(blank=True, max_length=255, null=True)),
                ('signed', models.BooleanField(default=False)),
                ('passport_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.passportdetails')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='contract',
            field=models.ManyToManyField(blank=True, to='client.contract'),
        ),
        migrations.AddField(
            model_name='client',
            name='passport_details',
            field=models.ManyToManyField(blank=True, null=True, to='client.passportdetails'),
        ),
    ]