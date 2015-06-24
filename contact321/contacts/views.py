from contacts.models import Contact, Phone
from contacts.serializers import ContactSerializer, PhoneSerializer, \
    PhoneWithContactSerializer
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


class PhoneListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PhoneSerializer

    def initial(self, request, *args, **kwargs):
        self.contact = Contact.objects.get(pk=kwargs['contact_pk'])
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return self.contact.phones

    def perform_create(self, serializer):
        if self.request.user != self.contact.owner:
            raise PermissionDenied
        serializer.save(contact=self.contact)


class PhoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          OwnsRelatedContact)
    serializer_class = PhoneWithContactSerializer
    queryset = Phone.objects.all()
