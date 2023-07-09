from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers

from support_request.models import SupportRequest


class SupportRequestSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SupportRequest
        fields = ('id', 'number', 'created_at', 'short_description', 'author', 'status', 'decision',
                  'state', 'deadline', 'closed', 'description', 'contact')

    status = serializers.CharField(label='статус', source='get_status_display')

