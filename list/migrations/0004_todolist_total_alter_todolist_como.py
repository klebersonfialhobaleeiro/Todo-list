# Generated by Django 4.1.4 on 2023-01-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_remove_todolist_status_todolist_como_delete_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='total',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='como',
            field=models.CharField(choices=[('FA', '⛔️ a Fazer'), ('RE', '⚠️ Fazendo'), ('FI', '✅ Finalizado')], default='FA', max_length=2),
        ),
    ]
