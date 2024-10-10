from django.db import models

from products.models import Coffee, Food
from users.models import CoffeeUser


class Order(models.Model):
    coffe_id = models.ForeignKey(
        Coffee, verbose_name="id кофе", on_delete=models.DO_NOTHING
    )
    food_id = models.ForeignKey(
        Food, verbose_name="id еды", on_delete=models.DO_NOTHING, null=True, blank=True
    )
    price = models.PositiveIntegerField(verbose_name="Общая цена")
    bonuses = models.DecimalField(
        verbose_name="Общий бонус", max_digits=2, decimal_places=1
    )
    is_paid = models.BooleanField(verbose_name="Заказ оплачен", default=False)
    is_ready = models.BooleanField(verbose_name="Заказ готов", default=False)
    user_id = models.OneToOneField(
        CoffeeUser, verbose_name="id клиента", on_delete=models.CASCADE
    )

    def __repr__(self) -> str:
        return f"<Order: {self.id}-{self.user_id}>"

    def __str__(self) -> str:
        return f"{self.id}-{self.user_id}"

    class Meta:
        ordering = ["id"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Mixin(models.Model):
    order_id = models.OneToOneField(
        Order, verbose_name="id заказа", on_delete=models.CASCADE
    )
    milk = models.BooleanField(verbose_name="Молоко", default=False)
    cinnamon = models.BooleanField(verbose_name="Корица", default=False)
    syrup = models.BooleanField(verbose_name="Сироп", default=False)

    def __str__(self) -> str:
        return f"{self.id}-{self.order_id}"

    def __repr__(self) -> str:
        return f"<Mixin: {self.id}-{self.order_id}>"

    class Meta:
        ordering = ["id"]
        verbose_name = "Добавка"
        verbose_name_plural = "Добавки"
