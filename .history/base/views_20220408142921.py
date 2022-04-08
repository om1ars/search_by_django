from django.shortcuts import render
from django.contrib.auth.views import LoginView
class CustomLogin(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reserver_lazy("tasks")
    

class TaskList(LoginReui)