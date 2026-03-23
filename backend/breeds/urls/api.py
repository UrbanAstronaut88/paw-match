from django.urls import path
from rest_framework.routers import DefaultRouter

from breeds.views import (
    BreedViewSet,
    MatchView,
    AddFavoriteView,
    RemoveFavoriteView,
    QuizResultListView,
    FavoriteListView,
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

    path(
        "quiz-results/",
        QuizResultListView.as_view(),
        name="quiz-results"
    ),

    path(
        "favorites/",
        FavoriteListView.as_view(),
        name="favorites"
    ),
]

urlpatterns += router.urls
