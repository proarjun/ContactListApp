from django.shortcuts import render
from rest_framework import generics 
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions
# Create your views here.

class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.all().filter(owner=self.request.user)
    
class DetailViewList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user).all()




