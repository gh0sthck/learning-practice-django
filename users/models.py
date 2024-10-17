from django.db import models
from django.contrib.auth.models import AbstractUser


class CoffeeUser(AbstractUser):
    username = models.CharField(
        max_length=128, verbose_name="Имя пользователя", null=False, unique=True
    )
    name = models.CharField(max_length=128, verbose_name="Имя", null=False)
    email = models.EmailField(verbose_name="Почта", null=False)
    bonus = models.DecimalField(
        verbose_name="Баллы", default=0, max_digits=2, decimal_places=1
    )
    balance = models.DecimalField(
        verbose_name="Баланс", default=0, max_digits=10, decimal_places=2
    )
    is_barista = models.BooleanField(verbose_name="Бариста", default=False)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<CoffeeUser: {self.username}>"

    class Meta:
        ordering = ["name"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
