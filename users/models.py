from django.db import models
from django.contrib.auth.models import AbstractUser


class UserTypes(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя", null=False)

    class Meta:
        ordering = ["name"]
        verbose_name = "Тип пользователя"
        verbose_name_plural = "Типы пользователей"


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
    user_type = models.ForeignKey(
        UserTypes,
        verbose_name="Тип пользователя",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<CoffeeUser: {self.name}>"

    class Meta:
        ordering = ["name"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
