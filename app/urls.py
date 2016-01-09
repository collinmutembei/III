from django.conf.urls import url, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'buckelists', views.BucketlistViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^buckelists/$', views.BucketlistViewset),
]
