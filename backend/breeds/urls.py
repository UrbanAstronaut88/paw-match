from rest_framework.routers import DefaultRouter

from .views import BreedViewSet


router = DefaultRouter()
router.register("breeds", BreedViewSet)

urlpatterns = router.urls
