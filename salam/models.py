from django.db import models

# Create your models here.
class info(models.Model):
    full_name=models.CharField(max_length=30)
    the_age=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=30)
