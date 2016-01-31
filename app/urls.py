from django.conf.urls import url, include
from rest_framework_extensions.routers import ExtendedSimpleRouter
from app import viewsets
from app.views import root_route, index

router = ExtendedSimpleRouter()

(
    router.register(r'bucketlists', viewsets.BucketlistViewset)
    .register(
        r'items',
        viewsets.ItemViewset,
        base_name='bucketlists-item',
        parents_query_lookups=['parent_bucketlist']
        )
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api/$', root_route),
    url(r'^auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^blst/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
