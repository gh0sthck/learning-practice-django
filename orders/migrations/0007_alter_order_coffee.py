# Generated by Django 5.1.1 on 2024-10-16 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_coffee_alter_order_food_and_more'),
        ('products', '0004_alter_coffee_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coffee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.coffee', verbose_name='Кофе'),
        ),
    ]
