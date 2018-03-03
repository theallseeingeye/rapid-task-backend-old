"""
The serializers.py depends on these models. Be sure to reflect the same changes on serializers.py
"""
from django.db import models
from ..core.models import TimeStampedModel


# To collect name and email from subscribers and allow options to receive newsletters.
class Subscriber(TimeStampedModel):
    email = models.EmailField(max_length=200, primary_key=True)
    name = models.CharField(max_length=100)
    subscribed = models.BooleanField(default=True)
    notes = models.TextField(max_length=2000)

    def __str__(self):
        return self.email
