from django.contrib.auth.models import User
from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description =models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    estimated_end = models.DateField(blank=True, null=True)
    priority = models.IntegerField(default=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.title