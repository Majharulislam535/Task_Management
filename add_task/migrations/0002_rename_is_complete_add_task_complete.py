# Generated by Django 5.0 on 2024-01-17 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_task',
            old_name='is_complete',
            new_name='complete',
        ),
    ]
