from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()


router.register("test", views.HouseViewSet)


urlpatterns = []


urlpatterns += router.urls
