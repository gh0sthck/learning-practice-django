from django.contrib import admin

from products.models import Coffee, Food


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ["name", "cost"]


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ["name", "cost"]
