from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from support_request.models import SupportRequest
from support_request.serializers import SupportRequestSerializer


# Create your views here.

class DefaultPagination(PageNumberPagination):
    page_size = 25
    max_page_size = 100
    page_size_query_param = 'page_size'


class SupportRequestViewSet(ModelViewSet):
    serializer_class = SupportRequestSerializer
    queryset = SupportRequest.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'contact', 'status']
    ordering_fields = ['created_at', 'number', 'closed', 'deadline']
    search_fields = ['number', 'author', 'contact', 'short_description']
    pagination_class = DefaultPagination

    @action(detail=False, url_path='fields', methods=['get'])
    def get_field_verbose_names(self, request, pk=None):
        serializer = self.get_serializer()
        fields = dict()
        for name, field in serializer.get_fields().items():
            fields[name] = dict()
            fields[name]['name'] = field.label or name.replace("_", " ")
            fields[name]['ordering'] = name in self.ordering_fields
        return Response(fields)
