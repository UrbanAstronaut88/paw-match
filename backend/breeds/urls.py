from django.urls import path
from .views import BreedListView, BreedDetailView


urlpatterns = [
    path("breeds/", BreedListView.as_view(), name="breeds-list"),
    path("breeds/<int:pk>/", BreedDetailView.as_view(), name="breed-detail"),
]
