from django.db import models
from datetime import date

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    phone2 = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()
    company = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(default=date.today)
    notes = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
