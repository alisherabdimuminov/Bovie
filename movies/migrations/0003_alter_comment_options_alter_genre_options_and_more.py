# Generated by Django 5.0.6 on 2024-06-21 19:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Izox', 'verbose_name_plural': 'Izoxlar'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Janr', 'verbose_name_plural': 'Janrlar'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Kino', 'verbose_name_plural': 'Kinolar'},
        ),
        migrations.AddField(
            model_name='movie',
            name='feedback',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, editable=False, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.IntegerField(verbose_name='Kino davomiyligi'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='ID'),
        ),
    ]
