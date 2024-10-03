from django.shortcuts import render, redirect
from django.contrib.auth import logout


def loging_view(request):
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("/")
