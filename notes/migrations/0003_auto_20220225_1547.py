# Generated by Django 2.2.6 on 2022-02-25 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20220225_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='tag',
            new_name='tags',
        ),
    ]
