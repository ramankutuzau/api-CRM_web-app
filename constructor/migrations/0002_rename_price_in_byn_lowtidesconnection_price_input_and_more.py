# Generated by Django 4.1.2 on 2023-07-21 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lowtidesconnection',
            old_name='price_in_byn',
            new_name='price_input',
        ),
        migrations.RenameField(
            model_name='lowtidesplug',
            old_name='price_in_byn',
            new_name='price_input',
        ),
        migrations.RenameField(
            model_name='mountingmaterials',
            old_name='price_in_byn',
            new_name='price_input',
        ),
        migrations.RenameField(
            model_name='windowsillconnection',
            old_name='price_in_byn',
            new_name='price_input',
        ),
        migrations.RenameField(
            model_name='windowsillplug',
            old_name='price_in_byn',
            new_name='price_input',
        ),
    ]