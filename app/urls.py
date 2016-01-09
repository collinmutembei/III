from django.conf.urls import url, include
from rest_framework import routers
from app import viewsets

router = routers.DefaultRouter()
router.register(r'buckelists', viewsets.BucketlistViewset)
router.register(r'items', viewsets.ItemViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^buckelists/$', viewsets.BucketlistViewset),
    url(r'^items/$', viewsets.ItemViewset),
]
