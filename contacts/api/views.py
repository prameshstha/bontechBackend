from rest_framework import generics

from contacts.api.serializer import ContactsSerializer
from contacts.models import Contacts


class AllContacts(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsEditDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer