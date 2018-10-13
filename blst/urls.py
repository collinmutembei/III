from django.urls import path
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
]
