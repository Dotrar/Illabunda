from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from . import views

app_name = "raven"

urlpatterns = [
    path("register", views.UserRegistrationView.as_view(), name="register"),
    path(
        "register/done",
        auth_views.PasswordResetDoneView.as_view(
            template_name="register/register_done.html"
        ),
        name="register-done",
    ),
    path(
        "register/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="register/register_confirm.html",
            success_url=reverse_lazy("hirundo_neoxena:register-complete"),
        ),
        name="register-confirm",
    ),
    path(
        "register/complete",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="register/register_complete.html"
        ),
        name="register-complete",
    ),
]
