# Generated by Django 5.1.1 on 2024-10-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_coffeeuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertypes',
            name='is_barista',
            field=models.BooleanField(default=False, verbose_name='Бариста'),
        ),
        migrations.AddField(
            model_name='usertypes',
            name='is_personal',
            field=models.BooleanField(default=False, verbose_name='Персонал'),
        ),
    ]
