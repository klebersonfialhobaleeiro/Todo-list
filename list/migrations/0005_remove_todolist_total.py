# Generated by Django 4.1.4 on 2023-01-17 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_todolist_total_alter_todolist_como'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='total',
        ),
    ]