from django.db import models
from django.contrib.au

class Task(models.Model):
    user = models.ForeignKey(User, )