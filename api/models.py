from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile', on_delete=models.PROTECT)
    avatar = models.TextField()


class Bucketlist(models.Model):
    """Bucketlist model"""

    name = models.CharField(blank=False, max_length=45, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.id, self.name)


class Item(models.Model):
    """Items model"""

    name = models.CharField(blank=False, max_length=45, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    parent_bucketlist = models.ForeignKey(
        Bucketlist,
        on_delete=models.CASCADE,
        related_name="items"
    )

    def __str__(self):
        return "{0} - {1}".format(self.id, self.name)
