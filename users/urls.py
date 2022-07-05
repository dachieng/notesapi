from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.UserRegistration.as_view(), name="register"),
    path("logout/", views.BlackListTokenView.as_view(), name="logout")
]


