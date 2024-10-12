from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from users.forms import UserRegisterForm
from users.models import CoffeeUser


class RegisterView(FormView):
    model = CoffeeUser
    form_class = UserRegisterForm
    success_url = reverse_lazy("main")
    template_name = "user_register.html"


class ProfileView(DetailView):
    model = CoffeeUser
    template_name = "user_profile.html"
    context_object_name = "user"
    success_url = reverse_lazy("main")
