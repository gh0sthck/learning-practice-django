# Generated by Django 5.1.4 on 2024-12-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_coffeeuser_email_verified_alter_coffeeuser_bonus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeeuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Почта'),
        ),
    ]