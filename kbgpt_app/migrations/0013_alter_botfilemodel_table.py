# Generated by Django 4.2.3 on 2023-07-29 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kbgpt_app', '0012_alter_botfilemodel_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='botfilemodel',
            table='bots_files',
        ),
    ]
