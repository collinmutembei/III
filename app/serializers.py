from rest_framework import serializers
from app.models import Bucketlist, Item


date_created = serializers.DateTimeField()
date_modified = serializers.DateTimeField()


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'date_created', 'date_modified', 'done', 'parent_bucketlist')

    def get_fields(self, *args, **kwargs):
        fields = super(ItemSerializer, self).get_fields(*args, **kwargs)
        if self.context:
            user = self.context['request'].user
            bucketlists = Bucketlist.objects.filter(
                created_by=user.id).values_list('id', flat=True)
            fields['parent_bucketlist'].queryset = fields['parent_bucketlist'].queryset.filter(
                id__in=bucketlists).all()
        return fields


class BucketlistSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'items', 'date_created', 'date_modified', 'created_by')
