from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=100, null=False)
