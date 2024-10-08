from django.contrib import admin

from users.models import CoffeeUser, UserTypes


@admin.register(CoffeeUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "balance"]


@admin.register(UserTypes)
class UserTypesAdmin(admin.ModelAdmin):
    list_display = ["name"]
