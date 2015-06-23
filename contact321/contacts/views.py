from contacts.models import Contact, Phone
from contacts.serializers import ContactSerializer, PhoneSerializer
from contacts.permissions import IsOwnerOrReadOnly, OwnsRelatedContact
from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PhoneCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PhoneSerializer

    def perform_create(self, serializer):
        contact = serializer.validated_data['contact']
        if self.request.user != contact.owner:
            raise PermissionDenied
        serializer.save()


class PhoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          OwnsRelatedContact)
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()
