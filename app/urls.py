from django.conf.urls import url, include
from rest_framework_extensions.routers import ExtendedSimpleRouter
from app import viewsets

router = ExtendedSimpleRouter()

(
    router.register(r'bucketlists', viewsets.BucketlistViewset)
    .register(
        r'items',
        viewsets.ItemViewset,
        base_name='bucketlist-items',
        parents_query_lookups=['parent_bucketlist']
        )

)

router.register(r'items', viewsets.ItemViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api', include('rest_framework.urls', namespace='rest_framework')),
]
