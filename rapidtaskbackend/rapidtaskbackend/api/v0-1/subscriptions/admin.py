from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribed', 'notes', 'date_created')


admin.site.register(Subscriber, SubscriberAdmin)
