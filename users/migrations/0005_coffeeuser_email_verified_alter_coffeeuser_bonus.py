# Generated by Django 5.1.3 on 2024-12-12 14:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_coffeeuser_user_type_coffeeuser_is_barista_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeeuser',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Подтвержден email'),
        ),
        migrations.AlterField(
            model_name='coffeeuser',
            name='bonus',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, validators=[django.core.validators.MaxValueValidator(limit_value=0.9)], verbose_name='Баллы'),
        ),
    ]
