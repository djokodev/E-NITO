from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.loging_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("accounts/", include("allauth.urls")),
]
