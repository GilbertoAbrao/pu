# Generated by Django 4.2.3 on 2023-07-28 20:32

from django.db import migrations, models
import django.db.models.deletion
import kbgpt_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('kbgpt_app', '0010_alter_botfilesmodel_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.FileField(upload_to=kbgpt_app.models.user_directory_path)),
                ('status', models.CharField(choices=[('processing', 'Processing'), ('done', 'Done'), ('error', 'Error')], default='processing', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kbgpt_app.botmodel')),
            ],
            options={
                'verbose_name': 'BotFile',
                'verbose_name_plural': 'BotsFiles',
                'db_table': 'bots_files',
            },
        ),
        migrations.DeleteModel(
            name='BotFilesModel',
        ),
    ]
