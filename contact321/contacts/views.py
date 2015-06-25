from contacts.models import Contact, Phone, Email
from contacts.serializers import ContactSerializer, PhoneSerializer, \
    PhoneWithContactSerializer, EmailSerializer, EmailWithContactSerializer
from contacts.permissions import IsOwnerOrReadOnly, OwnsRelatedContact
from django.db.models import Count
from rest_framework import viewsets, permissions, generics, filters
from rest_framework.exceptions import PermissionDenied
import django_filters


class ContactFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name="name", lookup_type="icontains")
    notes = django_filters.CharFilter(name="notes", lookup_type="icontains")

    class Meta:
        model = Contact
        fields = ['name', 'notes']


class ContactViewSet(viewsets.ModelViewSet):
    """Use name and notes GET parameters to filter."""
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ContactFilter

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
        return self.contact.phones.all()

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
        return self.contact.emails.all()

    def perform_create(self, serializer):
        if self.request.user != self.contact.owner:
            raise PermissionDenied
        serializer.save(contact=self.contact)


class EmailDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          OwnsRelatedContact)
    serializer_class = EmailWithContactSerializer
    queryset = Email.objects.all()
