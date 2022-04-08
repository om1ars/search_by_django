from django.db import models
from django.contrib.auth.mo

class Task(models.Model):
    user = models.ForeignKey(User, )