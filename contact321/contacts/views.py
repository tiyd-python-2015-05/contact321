from contacts.models import Contact
from contacts.serializers import ContactSerializer, UserSerializer
from contacts.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
