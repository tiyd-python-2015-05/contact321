from contacts.models import Contact
from contacts.serializers import ContactSerializer
from rest_framework import viewsets


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
