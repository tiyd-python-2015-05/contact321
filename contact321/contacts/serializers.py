from contacts.models import Contact
from django.contrib.auth.models import User
from rest_framework import serializers

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    phone_number = serializers.CharField(source='phone')
    _url = serializers.HyperlinkedIdentityField(view_name='contact-detail')

    class Meta:
        model = Contact
        fields = ('id', '_url', 'name', 'phone_number', 'email', 'owner')