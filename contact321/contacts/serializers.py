from contacts.models import Contact, Email, Phone
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.reverse import reverse


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = ('url', 'email', 'kind')


class EmailWithContactSerializer(serializers.HyperlinkedModelSerializer):
    contact = serializers.HyperlinkedRelatedField(read_only=True,
                                                  view_name='contact-detail')

    class Meta:
        model = Email
        fields = ('url', 'email', 'kind', 'contact')


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = ('url', 'phone', 'kind')


class PhoneWithContactSerializer(serializers.HyperlinkedModelSerializer):
    contact = serializers.HyperlinkedRelatedField(read_only=True,
                                                  view_name='contact-detail')

    class Meta:
        model = Phone
        fields = ('url', 'phone', 'kind', 'contact')


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    emails = EmailSerializer(many=True, read_only=True)
    phones = PhoneSerializer(many=True, read_only=True)
    _links = SerializerMethodField()

    def get__links(self, obj):
        links = {
            "phones": reverse('phone-list', kwargs=dict(contact_pk=obj.pk),
                              request=self.context.get('request')),
            "emails": reverse('email-list', kwargs=dict(contact_pk=obj.pk),
                              request=self.context.get('request'))}
        return links

    class Meta:
        model = Contact
        fields = (
            'id', 'url', 'name', 'website', 'notes', 'owner', 'emails',
            'phones', '_links')
