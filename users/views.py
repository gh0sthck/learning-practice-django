from django import forms
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth import login

from users.forms import UserRegisterForm
from users.models import CoffeeUser

from django_email_verification import send_email


def verify_email(request: HttpRequest):
    if not request.user.email_verified: 
        send_email(request.user) 
        return render(request, "user_email_sent.html")
    return redirect("main")


class RegisterView(FormView):
    model = CoffeeUser
    form_class = UserRegisterForm
    success_url = reverse_lazy("main")
    template_name = "user_register.html"

    def form_valid(self, form: forms.Form):
        saved_user = form.save(commit=False)
        saved_user.set_password(saved_user.password)
        saved_user.save()
        login(self.request, user=saved_user)
        return redirect("verify_email")

class ProfileView(DetailView):
    model = CoffeeUser
    template_name = "user_profile.html"
    context_object_name = "user"
    success_url = reverse_lazy("main")


class ProfileUpdateView(UpdateView):
    model = CoffeeUser
    template_name = "user_edit.html"
    context_object_name = "edited_user"
    fields = ["username", "name", ]
