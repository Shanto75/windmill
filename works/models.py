from django.db import models

# Create your models here.

class About(models.Model):
    about = models.CharField(max_length=255)