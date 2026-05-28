from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, RegisterView

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"
    ),
    path("register/", RegisterView.as_view(), name="register"),
]
