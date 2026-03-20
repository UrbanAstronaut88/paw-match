from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    BreedViewSet,
    MatchView,
    AddFavoriteView,
    RemoveFavoriteView,
)


router = DefaultRouter()
router.register("breeds", BreedViewSet)

urlpatterns = [
    path("match/", MatchView.as_view(), name="match"),

    path(
        "breeds/<int:pk>/favorite/",
        AddFavoriteView.as_view(),
        name="add-favorite"
    ),
    path(
        "breeds/<int:pk>/unfavorite/",
        RemoveFavoriteView.as_view(),
        name="remove-favorite"
    ),
]

urlpatterns += router.urls
