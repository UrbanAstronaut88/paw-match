from typing import Any

from rest_framework import serializers

from .models import Breed, Favorite, QuizResult


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class QuizResultSerializer(serializers.ModelSerializer):
    size = serializers.IntegerField(min_value=1, max_value=3)
    energy = serializers.IntegerField(min_value=1, max_value=5)
    kids = serializers.IntegerField(min_value=1, max_value=5)
    housing_type = serializers.ChoiceField(choices=Breed.HousingType.choices)

    class Meta:
        model = QuizResult
        fields = ("id", "size", "energy", "kids", "housing_type", "created_at")
        read_only_fields = ("id", "created_at")

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        return attrs


class FavoriteSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = ("id", "breed")


class MatchRequestSerializer(serializers.Serializer):
    size = serializers.IntegerField(min_value=1, max_value=3)
    energy = serializers.IntegerField(min_value=1, max_value=5)
    kids = serializers.IntegerField(min_value=1, max_value=5)
    housing_type = serializers.ChoiceField(choices=Breed.HousingType.choices)
