from .models import Subscriber
from .serializers import SubscriberSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics


class SubscriberCreate(generics.CreateAPIView):
    """
    Post:
    Creates a new subscriber
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = (AllowAny, )

class SubscriberList(generics.ListAPIView):
    """
    Shows list of subscribers
    """
    # queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        queryset = Subscriber.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset
