from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.response import Response
from .custom_auth import CustomAuthentication
from rest_framework.pagination import PageNumberPagination


class ContactPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'
    page_size_query_param = 'page_size'


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = (CustomAuthentication,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'email',)

    def create(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            contact = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            contact = self.get_object()
            contact.delete()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
