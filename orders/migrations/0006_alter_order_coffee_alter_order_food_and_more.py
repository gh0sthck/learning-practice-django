# Generated by Django 5.1.1 on 2024-10-15 12:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_order_id_mixin_order_and_more'),
        ('products', '0004_alter_coffee_volume'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coffee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.coffee', verbose_name='Кофе'),
        ),
        migrations.AlterField(
            model_name='order',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.food', verbose_name='Еда'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_bonus_used',
            field=models.BooleanField(default=False, verbose_name='Использовать бонус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
    ]
