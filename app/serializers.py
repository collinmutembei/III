from rest_framework import serializers
from app.models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified', 'created_by')
