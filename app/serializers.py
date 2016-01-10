from rest_framework import serializers
from app.models import Bucketlist, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'date_created', 'date_modified', 'done')


class BucketlistSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'items', 'date_created', 'date_modified', 'created_by')
