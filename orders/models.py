from django.db import models

from products.models import Coffee, Food
from users.models import CoffeeUser


class Order(models.Model):
    coffee = models.ForeignKey(
        Coffee, verbose_name="Кофе", on_delete=models.DO_NOTHING, null=True, blank=True
    )
    food = models.ForeignKey(
        Food, verbose_name="Еда", on_delete=models.DO_NOTHING, null=True, blank=True
    )
    is_paid = models.BooleanField(verbose_name="Заказ оплачен", default=False)
    is_ready = models.BooleanField(verbose_name="Заказ готов", default=False)
    user = models.OneToOneField(
        CoffeeUser, verbose_name="Клиент", on_delete=models.CASCADE
    )
    is_bonus_used = models.BooleanField(
        verbose_name="Использовать бонус", default=False
    )

    def __repr__(self) -> str:
        return f"<Order: {self.id}-{self.user}>"

    def __str__(self) -> str:
        return f"{self.id}-{self.user}"

    def get_bonuses(self) -> float:
        if self.food:
            return (self.food.cost / 100) + (self.coffee.cost / 100)
        return self.coffee / 100

    def pay_order(self):
        price = self.price

        if self.is_bonus_used:
            price -= price * self.user.bonus

        if self.user.balance >= price:
            self.user.balance -= price
            self.is_paid = True
            self.user.bonus += self.get_bonuses()
        return self.is_paid

    def get_total_price(self):
        if self.food:
            return self.coffee.cost + self.food.cost
        return self.coffee.cost

    class Meta:
        ordering = ["id"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Mixin(models.Model):
    order = models.OneToOneField(
        Order, verbose_name="id заказа", on_delete=models.CASCADE
    )
    milk = models.BooleanField(verbose_name="Молоко", default=False)
    cinnamon = models.BooleanField(verbose_name="Корица", default=False)
    syrup = models.BooleanField(verbose_name="Сироп", default=False)

    def __str__(self) -> str:
        return f"{self.id}-{self.order}"

    def __repr__(self) -> str:
        return f"<Mixin: {self.id}-{self.order}>"

    class Meta:
        ordering = ["id"]
        verbose_name = "Добавка"
        verbose_name_plural = "Добавки"
