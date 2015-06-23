from contacts.models import Contact
from contacts.serializers import ContactSerializer
from contacts.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)