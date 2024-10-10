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
    is_paid = models.BooleanField(verbose_name="Заказ оплачен", default=False)
    is_ready = models.BooleanField(verbose_name="Заказ готов", default=False)
    user_id = models.OneToOneField(
        CoffeeUser, verbose_name="id клиента", on_delete=models.CASCADE
    )
    is_bonus_used = models.BooleanField(verbose_name="Использовать бонс", default=False)

    def __repr__(self) -> str:
        return f"<Order: {self.id}-{self.user_id}>"

    def __str__(self) -> str:
        return f"{self.id}-{self.user_id}"

    def get_bonuses(self) -> float:
        if self.food_id:
            return (self.food_id.cost / 100) + (self.coffe_id.cost / 100)
        return self.coffe_id / 100

    def pay_order(self):
        price = self.price

        if self.is_bonus_used:
            price -= price * self.user_id.bonus

        if self.user_id.balance >= price:
            self.user_id.balance -= price
            self.is_paid = True
            self.user_id.bonus += self.get_bonuses()
        return self.is_paid

    def get_total_price(self):
        if self.food_id:
            return self.coffe_id.cost + self.food_id.cost
        return self.coffe_id.cost

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
