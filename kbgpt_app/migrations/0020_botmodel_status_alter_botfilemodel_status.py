# Generated by Django 4.2.3 on 2023-08-01 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbgpt_app', '0019_botfilemodel_callback_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='botmodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=50),
        ),
        migrations.AlterField(
            model_name='botfilemodel',
            name='status',
            field=models.CharField(choices=[('processing', 'Processing'), ('done', 'Done'), ('error', 'Error')], default='processing', max_length=50),
        ),
    ]
