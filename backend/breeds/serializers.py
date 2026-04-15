from typing import Any

from rest_framework import serializers

from .models import Breed, Favorite, QuizResult


class BreedSerializer(serializers.ModelSerializer):
    traits = serializers.SerializerMethodField()

    class Meta:
        model = Breed
        fields = ("id", "name", "description", "image_url", "traits")

    def get_traits(self, obj: Breed) -> dict[str, dict[str, Any]]:
        return {
            "size": {
                "value": obj.size,
                "label": obj.get_size_display(),
            },
            "energy": {
                "value": obj.energy,
                "label": obj.get_energy_display(),
            },
            "grooming": {
                "value": obj.grooming,
                "label": obj.get_grooming_display(),
            },
            "kids_friendly": {
                "value": obj.kids_friendly,
                "label": obj.get_kids_friendly_display(),
            },
            "housing_type": {
                "value": obj.housing_type,
                "label": obj.get_housing_type_display(),
            },
        }


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
