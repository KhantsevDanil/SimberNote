# Generated by Django 2.2.6 on 2022-02-25 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='tags',
        ),
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.ManyToManyField(related_name='notes', to='notes.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='note',
            name='author',
            field=models.ForeignKey(help_text='author name', on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL, verbose_name='author name'),
        ),
    ]
