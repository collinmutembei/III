from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, unique=True, related_name="profile", on_delete=models.CASCADE
    )
    avatar = models.TextField()

    def __str__(self):
        return "<UserProfile for User with id {user_id}".format(user_id=self.user.id)


class Bucketlist(models.Model):
    """Bucketlist model"""

    name = models.CharField(blank=False, max_length=45)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Bucketlist"
        unique_together = ("name", "created_by")

    def __str__(self):
        return "{0} - {1}".format(self.id, self.name)


class Item(models.Model):
    """Items model"""

    name = models.CharField(blank=False, max_length=45)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    parent_bucketlist = models.ForeignKey(
        Bucketlist, on_delete=models.CASCADE, related_name="items"
    )

    class Meta:
        verbose_name = "Bucketlist Item"
        unique_together = ("name", "parent_bucketlist")

    def __str__(self):
        return "{0} - {1}".format(self.id, self.name)
