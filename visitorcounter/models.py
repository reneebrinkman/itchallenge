from django.db import models

# Create your models here.
class VisitorLog(models.Model):
    first_name = models.CharField(max_length=30, default="user")
