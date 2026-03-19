from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BreedViewSet, MatchView


router = DefaultRouter()
router.register("breeds", BreedViewSet)

urlpatterns = [
    path("match/", MatchView.as_view(), name="match")
]

urlpatterns += router.urls
