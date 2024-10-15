from django import forms

from users.models import CoffeeUser


class UserRegisterForm(forms.ModelForm):
    password_repeat = forms.CharField(
        min_length=8, label="Повторение пароля", widget=forms.PasswordInput
    )

    class Meta:
        model = CoffeeUser
        fields = ["username", "name", "email", "password"]
        widgets = {"password": forms.PasswordInput()}

    def clean_password_repeat(self) -> bool:
        data = self.cleaned_data
        if data["password_repeat"] == data["password"]:
            return data
        raise forms.ValidationError("Пароли не совпадают")
