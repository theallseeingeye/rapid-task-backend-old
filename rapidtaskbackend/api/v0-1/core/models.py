'''
This is where the base models will be if it ties across all the apps
'''
from django.db import models


class TimeStampedModel(models.Model):
    # A timestamp representing when the object was created.
    date_created = models.DateTimeField(auto_now_add=True)
    # A timestamp representing when the object was updated.
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        # ordering = ['-date_created', '-date_updated']
