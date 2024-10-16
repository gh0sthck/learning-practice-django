from orders.models import Mixin
from django import forms


class AddMixinForm(forms.ModelForm):
    class Meta:
        model = Mixin
        fields = ["milk", "cinnamon", "syrup"]
