from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from users.views import ProfileUpdateView, ProfileView, RegisterView, change_password, verify_email

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="user_login.html", next_page=reverse_lazy("main")
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("main")), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
    path("edit/<int:pk>", ProfileUpdateView.as_view(), name="edit_profile"),
    path("verify_email/", verify_email, name="verify_email"),
    path("change_password/", change_password, name="change_password")
]
