from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_spectacular.utils import extend_schema

from .models import Breed, Favorite, QuizResult
from .serializers import BreedSerializer, QuizResultSerializer, FavoriteSerializer, MatchRequestSerializer
from .services.matching import get_best_matches



class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all().order_by("name")
    serializer_class = BreedSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["size", "energy", "kids_friendly", "housing_type"]


class MatchView(APIView):
    @extend_schema(
        request=MatchRequestSerializer,
        responses={200: BreedSerializer(many=True)},
    )

    def post(self, request: Request) -> Response:
        serializer = MatchRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_data = serializer.validated_data

        breeds = Breed.objects.all()
        matches = get_best_matches(user_data, breeds)

        result = [
            {
                "breed": match["breed"].name,
                "score": match["score"],
                "match": match["match"],
            }
            for match in matches
        ]

        return Response(result)


class AddFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, pk: int) -> Response:
        breed = get_object_or_404(Breed, pk=pk)

        obj, created = Favorite.objects.get_or_create(
            user=request.user,
            breed=breed
        )

        return Response({
            "status": "added",
            "created": created
        })


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
