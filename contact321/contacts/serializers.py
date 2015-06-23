from contacts.models import Contact, Email, Phone
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('kind', 'email')


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('kind', 'phone')


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    emails = EmailSerializer(many=True, read_only=True)
    phones = PhoneSerializer(many=True, read_only=True)
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    class Meta:
        model = Contact
