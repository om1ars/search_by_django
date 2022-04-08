from django.urls import path
from .views import CustomLoginView, TaskList

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("", TaskList.as_view(), name="tasks")
]
