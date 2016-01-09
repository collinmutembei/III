from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Bucketlist(models.Model):
    """Bucketlist model"""

    name = models.CharField(blank=False, max_length=45)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User)

    def __str__(self):
        return self.name
