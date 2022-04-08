from django.db import models
from django.contrib.

class Task(models.Model):
    user = models.ForeignKey(User, )