from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()


router.register("users", views.UserViewSet)


urlpatterns = [
    path(
        "change-password/<str:token>/",
        views.UserViewSet.as_view({"post": "change_password"}),
        name="users-change-password",
    ),
]


urlpatterns += router.urls
