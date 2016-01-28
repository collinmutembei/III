from rest_framework import viewsets, permissions
from rest_framework_extensions.mixins import NestedViewSetMixin
from app.models import Bucketlist, Item
from app.permissions import IsOwner
from app.serializers import BucketlistSerializer, ItemSerializer


class BucketlistViewset(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_active:
            return Bucketlist.objects.filter(created_by=user.id)
        return Bucketlist.objects.all()


class ItemViewset(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated,)
