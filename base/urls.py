from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include("bulletin_board.urls")),
    path("", include("users.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, doculment_root=settings.MEDIA_ROOT)
