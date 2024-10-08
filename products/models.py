from django.db import models
from django.urls import reverse


class Coffee(models.Model):
    name = models.CharField(max_length=90, verbose_name="Название", null=False)
    cost = models.PositiveIntegerField(verbose_name="Цена")

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"<Coffe: {self.name}>"

    def get_absolute_url(self):
        return reverse(kwargs={"pk": self.pk})

    class Meta:
        ordering = ["name"]
        verbose_name = "Кофе"
        verbose_name_plural = "Кофе"


class Food(models.Model):
    name = models.CharField(max_length=90, verbose_name="Название", null=False)
    cost = models.PositiveIntegerField(verbose_name="Цена")

    def get_absolute_url(self):
        return reverse(kwargs={"pk": self.pk})
    
    def __repr__(self):
        return f"<Food: {self.name}>"

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Еда"
        verbose_name_plural = "Еда"