from rest_framework import viewsets
from app.models import Bucketlist, Item
from app.serializers import BucketlistSerializer, ItemSerializer


class BucketlistViewset(viewsets.ModelViewSet):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
