from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Breed, Favorite, QuizResult
from .serializers import BreedSerializer, QuizResultSerializer, FavoriteSerializer
from .services.matching import get_best_matches



class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["size", "energy", "kids_friendly", "housing_type"]


class MatchView(APIView):

    def post(self, request: Request) -> Response:

        user_data: dict = request.data

        QuizResult.objects.create(
            user=request.user if request.user.is_authenticated else None,
            size=user_data["size"],
            energy=user_data["energy"],
            kids=user_data["kids"],
            housing=user_data["housing"],
        )

        breeds = Breed.objects.all()

        matches = get_best_matches(user_data, breeds)

        result: list[dict] = []

        for item in matches:
            breed_data = BreedSerializer(item["breed"]).data
            breed_data["score"] = item["score"]
            result.append(breed_data)

        return Response(result, status=status.HTTP_200_OK)


class AddFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, pk: int) -> Response:
        breed = Breed.objects.get(pk=pk)

        Favorite.objects.get_or_create(
            user=request.user,
            breed=breed
        )

        return Response({"status": "added"})


class RemoveFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request, pk: int) -> Response:

        Favorite.objects.filter(
            user=request.user,
            breed_id=pk
        ).delete()

        return Response({"status": "removed"})


class QuizResultListView(ListAPIView):

    serializer_class = QuizResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return QuizResult.objects.filter(user=self.request.user).order_by("-created_at")


class FavoriteListView(ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet[Favorite]:
        return Favorite.objects.filter(user=self.request.user)
