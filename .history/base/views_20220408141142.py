from django.shortcuts import render
from django.contrib.auth.views import LoginView
class CustomLogin(LoginView):
    template_name = "base\login"