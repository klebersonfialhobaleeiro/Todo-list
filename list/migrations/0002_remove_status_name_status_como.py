# Generated by Django 4.1.4 on 2023-01-05 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='name',
        ),
        migrations.AddField(
            model_name='status',
            name='como',
            field=models.CharField(choices=[('FA', '⛔️ a Fazer'), ('RE', '⚠️ Fazendo'), ('FI', '✅ Finalizado')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
