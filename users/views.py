from django import forms
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login

from users.forms import UserRegisterForm
from users.models import CoffeeUser


class RegisterView(FormView):
    model = CoffeeUser
    form_class = UserRegisterForm
    success_url = reverse_lazy("main")
    template_name = "user_register.html"

    def form_valid(self, form: forms.Form):
        saved_user = form.save(commit=False)
        print("SAVED", saved_user, type(saved_user))
        saved_user.set_password(saved_user.password)
        print("PASSWD", saved_user.password)
        saved_user.save()
        user = authenticate(
            username=saved_user.username,
            password=saved_user.password,
        )
        if user:
            login(self.request, user=user)
        return redirect("main")


class ProfileView(DetailView):
    model = CoffeeUser
    template_name = "user_profile.html"
    context_object_name = "user"
    success_url = reverse_lazy("main")
