from rest_framework import serializers
from .models import Subscriber


"""
These are regular simple serializers with no relationships
"""


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'email',
            'name',
            'subscribed',
        )
