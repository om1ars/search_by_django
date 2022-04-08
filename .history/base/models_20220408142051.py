from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, )