from rest_framework import viewsets
from rest_framework import permissions
from api.v1.serializers import ContactSerializer

from .models import Contact

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer