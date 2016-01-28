from rest_framework import permissions
from app.models import Item


class IsOwner(permissions.BasePermission):
    """
    custom permissions for owners
    """

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Item):
            return obj.parent_bucketlist.created_by == request.user
        return obj.created_by == request.user
