from django import forms

from users.models import CoffeeUser


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = CoffeeUser
        fields = "__all__"
