from decimal import Decimal
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class CoffeeUser(AbstractUser):
    username = models.CharField(
        max_length=128, verbose_name="Имя пользователя", null=False, unique=True
    )
    name = models.CharField(max_length=128, verbose_name="Имя", null=False)
    email = models.EmailField(verbose_name="Почта", null=False, unique=True)
    bonus = models.DecimalField(
        verbose_name="Баллы",
        default=0,
        max_digits=2,
        decimal_places=1,
        validators=[MaxValueValidator(limit_value=0.9)],
    )
    balance = models.DecimalField(
        verbose_name="Баланс", default=0, max_digits=10, decimal_places=2
    )
    is_barista = models.BooleanField(verbose_name="Бариста", default=False)
    email_verified = models.BooleanField(verbose_name="Подтвержден email", default=False)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<CoffeeUser: {self.username}>"

    def pay_order(self, total_price: int):
        if total_price > 180:
            self.balance -= total_price - self.bonus * total_price
            self.bonus = 0
        else:
            self.balance -= total_price
        self.bonus += Decimal(0.3)

    class Meta:
        ordering = ["name"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
