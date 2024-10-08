# Generated by Django 5.1.1 on 2024-10-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_coffee_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='Объем'),
        ),
    ]
