from rest_framework import viewsets
from app.models import Bucketlist, Item
from app.serializers import BucketlistSerializer, ItemSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin


class BucketlistViewset(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class ItemViewset(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
