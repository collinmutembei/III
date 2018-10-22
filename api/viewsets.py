from rest_framework import viewsets, permissions
from rest_framework_extensions.mixins import NestedViewSetMixin
from api.models import Bucketlist, Item
from api.permissions import IsOwner
from api.serializers import BucketlistSerializer, ItemSerializer


class BucketlistViewset(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_active:
            return Bucketlist.objects.filter(created_by=user.id)


class ItemViewset(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated)
