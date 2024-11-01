from .models import Coffee
from django import forms


class AddMixinForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ["milk", "cinnamon", "syrup"]
