# Generated by Django 4.2.3 on 2023-07-06 20:49

from django.db import migrations, models
import kbgpt_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('kbgpt_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='group',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='path',
            field=models.FileField(upload_to=kbgpt_app.models.user_directory_path),
        ),
    ]
