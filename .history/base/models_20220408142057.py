from django.db import models
from django.

class Task(models.Model):
    user = models.ForeignKey(User, )