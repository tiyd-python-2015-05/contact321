from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Email(models.Model):
    contact = models.ForeignKey(Contact, related_name="emails")
    email = models.EmailField()
    kind = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.email


class Phone(models.Model):
    contact = models.ForeignKey(Contact, related_name="phones")
    phone = models.CharField(max_length=20)
    kind = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.phone
