from django.contrib import admin

from orders.models import Mixin, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "price", "is_ready"]


@admin.register(Mixin)
class MixinAdmin(admin.ModelAdmin):
    list_display = ["id", "order_id"]
