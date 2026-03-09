from django.urls import path
from .views import BreedListView


urlpatterns = [
    path("breeds/", BreedListView.as_view(), name="breeds-list"),
]
