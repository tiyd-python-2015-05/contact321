from contacts.models import Contact
from rest_framework import serializers

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'url', 'name', 'phone', 'email')