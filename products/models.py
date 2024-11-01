from django.db import models
from django.urls import reverse


class Coffee(models.Model):
    name = models.CharField(max_length=90, verbose_name="Название", null=False)
    cost = models.PositiveIntegerField(verbose_name="Цена")
    volume = models.PositiveIntegerField(verbose_name="Объем (мл)", default=0)
    milk = models.BooleanField(verbose_name="Молоко", default=False)
    cinnamon = models.BooleanField(verbose_name="Корица", default=False)
    syrup = models.BooleanField(verbose_name="Сироп", default=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Coffee: {self.name}>"

    @property
    def as_dict(self) -> dict:
        return {
            "id": self.pk,
            "name": self.name,
            "cost": self.cost,
            "volume": self.volume,
        }

    @property
    def mixins_as_dict(self) -> dict:
        return { 
            "milk": self.milk,
            "cinnamon": self.cinnamon,
            "syrup": self.syrup,
        }

    def set_mixin(self, cinnamon=None, milk=None, syrup=None) -> None:
        self.cinnamon = cinnamon
        self.milk = milk
        self.syrup = syrup

    class Meta:
        ordering = ["name"]
        verbose_name = "Кофе"
        verbose_name_plural = "Кофе"


class Food(models.Model):
    name = models.CharField(max_length=90, verbose_name="Название", null=False)
    cost = models.PositiveIntegerField(verbose_name="Цена")

    def __repr__(self):
        return f"<Food: {self.name}>"

    def __str__(self):
        return self.name

    @property
    def as_dict(self) -> dict:
        return {"id": self.pk, "name": self.name, "cost": self.cost}

    class Meta:
        ordering = ["name"]
        verbose_name = "Еда"
        verbose_name_plural = "Еда"
