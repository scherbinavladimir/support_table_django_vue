from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
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
    filterset_fields = ['created_at', 'status']
    search_fields = ['number', 'author', 'contact', 'short_description']
    pagination_class = DefaultPagination
