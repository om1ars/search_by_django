from django.db import models
from django.contrib.auth.

class Task(models.Model):
    user = models.ForeignKey(User, )