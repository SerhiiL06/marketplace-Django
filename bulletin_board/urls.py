from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()


router.register("adv", views.HouseViewSet)


urlpatterns = []


urlpatterns += router.urls
