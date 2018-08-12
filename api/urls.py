from django.conf.urls import include, handler404
from django.urls import path
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_jwt.views import obtain_jwt_token
from api import viewsets
from api.views import root_route, landing, dashboard, logout

router = ExtendedSimpleRouter()

(
    router.register("bucketlists", viewsets.BucketlistViewset).register(
        "items",
        viewsets.ItemViewset,
        base_name="bucketlists-item",
        parents_query_lookups=["parent_bucketlist"],
    )
)

urlpatterns = [
    path("", landing),
    path("dashboard/", dashboard),
    path("logout/", logout),
    path("api/", include(router.urls)),
    path("api/", root_route),
    path("auth/login/", obtain_jwt_token),
    path("blst/", include("rest_framework.urls", namespace="rest_framework")),
    # path("docs/", include("rest_framework_swagger.urls")),
]
handler404 = "api.views.custom_404"
