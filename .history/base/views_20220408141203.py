from django.shortcuts import render
from django.contrib.auth.views import LoginView
class CustomLogin(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_field_name