from django.db import models
from django.contrib.auth.models impr

class Task(models.Model):
    user = models.ForeignKey(User, )