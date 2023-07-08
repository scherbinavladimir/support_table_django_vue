from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers

from support_request.models import SupportRequest


class SupportRequestSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SupportRequest
        fields = '__all__'
