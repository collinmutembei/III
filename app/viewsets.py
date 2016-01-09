from rest_framework import viewsets
from app.models import Bucketlist
from app.serializers import BucketlistSerializer


class BucketlistViewset(viewsets.ModelViewSet):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
