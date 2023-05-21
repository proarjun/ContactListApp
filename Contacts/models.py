from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    contact_picture = models.URLField(null=True, default="")
    is_favourite = models.BooleanField(default=False)
