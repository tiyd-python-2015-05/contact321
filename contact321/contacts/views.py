from contacts.models import Contact, Phone, Email
from contacts.serializers import ContactSerializer, PhoneSerializer, \
    PhoneWithContactSerializer, EmailSerializer, EmailWithContactSerializer
from contacts.permissions import IsOwnerOrReadOnly, OwnsRelatedContact
from django.db.models import Count
from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user).annotate(
            email_count=Count('emails', distinct=True),
            phone_count=Count('phones', distinct=True))

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


class EmailListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EmailSerializer

    def initial(self, request, *args, **kwargs):
        self.contact = Contact.objects.get(pk=kwargs['contact_pk'])
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return self.contact.emails

    def perform_create(self, serializer):
        if self.request.user != self.contact.owner:
            raise PermissionDenied
        serializer.save(contact=self.contact)


class EmailDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          OwnsRelatedContact)
    serializer_class = EmailWithContactSerializer
    queryset = Email.objects.all()
