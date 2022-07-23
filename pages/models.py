from django.db import models

# Create your models here.
class Messages(models.Model):
    uri = models.CharField(max_length=255, default="", unique=True)
