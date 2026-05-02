from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Breed, Favorite, QuizResult, BreedComparison
from .serializers import (
    BreedComparisonSerializer,
    BreedSerializer,
    FavoriteSerializer,
    MatchRequestSerializer,
    QuizResultSerializer,
)
from .services.matching import compare_breeds, get_best_matches


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all().order_by("name")
    serializer_class = BreedSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["size", "energy", "kids_friendly", "housing_type"]


class MatchView(APIView):
    @extend_schema(
        request=MatchRequestSerializer,
        responses={200: BreedSerializer(many=True)},
        description="Calculate best breed matches and save quiz result for authenticated users",
    )
    def post(self, request: Request) -> Response:
        serializer: MatchRequestSerializer = MatchRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data: dict = serializer.validated_data

        if request.user.is_authenticated:
            QuizResult.objects.create(
                user=request.user,
                size=user_data["size"],
                energy=user_data["energy"],
                kids=user_data["kids"],
                housing_type=user_data["housing_type"],
            )

        breeds: QuerySet[Breed] = Breed.objects.all()
        matches = get_best_matches(user_data, breeds)

        result: list[dict] = [
            {
                "id": match["breed"].id,
                "breed": match["breed"].name,
                "score": match["score"],
                "match": match["match"],
            }
            for match in matches
        ]

        return Response(result, status=status.HTTP_200_OK)


class BreedCompareView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="first",
                type=int,
                required=True,
                description="First breed ID"
            ),
            OpenApiParameter(
                name="second",
                type=int,
                required=True,
                description="Second breed ID"
            ),
        ],
        responses={200: BreedComparisonSerializer},
        description="Compare two dog breeds for frontend comparison page",
    )
    def get(self, request: Request) -> Response:
        first_id: str | None = request.query_params.get("first")
        second_id: str | None = request.query_params.get("second")

        if not first_id or not second_id:
            return Response(
                {"detail": "Both 'first' and 'second' query parameters are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if first_id == second_id:
            return Response(
                {"detail": "Please select two different breeds for comparison."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        first_breed: Breed = get_object_or_404(Breed, pk=first_id)
        second_breed: Breed = get_object_or_404(Breed, pk=second_id)

        comparison: BreedComparison | None = BreedComparison.objects.filter(
            first_breed=first_breed,
            second_breed=second_breed,
        ).first()

        if comparison is None:
            comparison = BreedComparison.objects.filter(
                first_breed=second_breed,
                second_breed=first_breed,
            ).first()

        conclusion: str = (
            comparison.conclusion
            if comparison
            else (
                f"{first_breed.name} і {second_breed.name} — These are different breeds, "
                "each with their own unique characteristics."
            )
        )

        result: dict = {
            "first_breed": first_breed,
            "second_breed": second_breed,
            "conclusion": conclusion,
        }

        serializer: BreedComparisonSerializer = BreedComparisonSerializer(
            result,
            context={"request": request},
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class AddFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: None},
        description="Add breed to favorites",
    )
    def post(self, request: Request, pk: int) -> Response:
        breed: Breed = get_object_or_404(Breed, pk=pk)

        _, created = Favorite.objects.get_or_create(
            user=request.user,
            breed=breed,
        )

        return Response(
            {
                "status": "added",
                "created": created,
            },
            status=status.HTTP_200_OK,
        )


class RemoveFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: None},
        description="Remove breed from favorites",
    )
    def delete(self, request: Request, pk: int) -> Response:
        Favorite.objects.filter(
            user=request.user,
            breed_id=pk,
        ).delete()

        return Response({"status": "removed"}, status=status.HTTP_200_OK)


class FavoriteListView(ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    queryset = Favorite.objects.none()

    def get_queryset(self) -> QuerySet[Favorite]:
        if getattr(self, "swagger_fake_view", False):
            return Favorite.objects.none()

        return Favorite.objects.filter(user=self.request.user)


class QuizResultViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = QuizResultSerializer
    queryset = QuizResult.objects.all().order_by("-created_at")

    def perform_create(self, serializer: QuizResultSerializer) -> None:
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)
