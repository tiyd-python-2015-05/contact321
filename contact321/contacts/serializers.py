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
    email_count = serializers.IntegerField(read_only=True)
    phones = PhoneSerializer(many=True, read_only=True)
    phone_count = serializers.IntegerField(read_only=True)
    _links = SerializerMethodField()

    def get__links(self, obj):
        links = {
            "phones": reverse('phone-list', kwargs=dict(contact_pk=obj.pk),
                              request=self.context.get('request')),
            "emails": reverse('email-list', kwargs=dict(contact_pk=obj.pk),
                              request=self.context.get('request'))}
        return links

    # How to prevent querysets not being annotated from blowing up:
    #
    # email_count = SerializerMethodField()
    # phone_count = SerializerMethodField()
    #
    # def get_email_count(self, obj):
    #     try:
    #         return obj.email_count
    #     except AttributeError:
    #         return obj.emails.count()
    #
    # def get_phone_count(self, obj):
    #     try:
    #         return obj.phone_count
    #     except AttributeError:
    #         return obj.phones.count()

    class Meta:
        model = Contact
        fields = (
            'id', 'url', 'name', 'website', 'notes', 'owner', 'emails',
            'phones', 'email_count', 'phone_count', '_links')
