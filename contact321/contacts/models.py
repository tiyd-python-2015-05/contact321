from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    owner = models.ForeignKey(User, related_name="contacts")
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()