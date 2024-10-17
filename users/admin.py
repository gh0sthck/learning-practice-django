from django.contrib import admin

from users.models import CoffeeUser


@admin.register(CoffeeUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "balance"]
