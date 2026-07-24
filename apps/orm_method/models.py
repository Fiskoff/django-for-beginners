from django.db import models
from django.utils import timezone

class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    work_experience = models.SmallIntegerField(default=0)