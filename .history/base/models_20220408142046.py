from django.db import models

class Task(models.Model):
    user = models.ForeignKey(to, on_delete)