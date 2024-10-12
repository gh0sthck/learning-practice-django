from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from users.views import ProfileView, RegisterView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="user_login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
]
