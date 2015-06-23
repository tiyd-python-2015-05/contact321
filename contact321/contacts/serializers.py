from contacts.models import Contact
from django.contrib.auth.models import User
from rest_framework import serializers

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Contact
        fields = ('id', 'url', 'name', 'phone', 'email', 'owner')