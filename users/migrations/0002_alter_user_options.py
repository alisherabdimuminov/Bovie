# Generated by Django 5.0.6 on 2024-06-21 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Foydalanuvchi', 'verbose_name_plural': 'Foydalanuvchilar'},
        ),
    ]
