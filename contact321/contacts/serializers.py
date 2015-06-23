from contacts.models import Contact, Email, Phone
from rest_framework import serializers

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    emails = EmailSerializer(many=True, read_only=True)
    phones = PhoneSerializer(many=True, read_only=True)

    _url = serializers.HyperlinkedIdentityField(view_name='contact-detail')

    class Meta:
        model = Contact
        fields = (
        'id', '_url', 'name', 'website', 'notes', 'owner', 'emails', 'phones')
