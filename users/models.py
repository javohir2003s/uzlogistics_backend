from datetime import timezone

from django.db import models
from django.template.defaultfilters import default


# Create your models here.


class User(models.Model):
    tg_id = models.BigIntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, unique=True)
    role = models.CharField(max_length=10, choices=[
        ('client', 'Client'),
        ('driver', 'Driver'),
        ('admin', 'Admin'),
        ('anonim', 'Anonymous'),
    ], default='anonim')
    language = models.CharField(max_length=10, choices=[
        ('uz', 'Uzbek'),
        ('ru', 'Russian'),
        ('en', 'English')
    ], default='uz')
    sub_start = models.DateTimeField(auto_now_add=True)
    sub_end = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[
        ('busy', 'Band'),
        ('free', "Bo'sh"),
    ], null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.role})"
