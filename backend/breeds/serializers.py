from typing import Any

from rest_framework import serializers

from .models import Breed, Favorite, QuizResult


class BreedSerializer(serializers.ModelSerializer):
    traits = serializers.SerializerMethodField()

    class Meta:
        model = Breed
        fields = (
            "id",
            "name",
            "description",
            "image_url",
            "image",
            "traits",
        )

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


class BreedCompareCardSerializer(serializers.ModelSerializer):
    image_src = serializers.SerializerMethodField()
    traits = serializers.SerializerMethodField()
    housing = serializers.SerializerMethodField()

    class Meta:
        model = Breed
        fields = (
            "id",
            "name",
            "image_src",
            "traits",
            "housing",
        )

    def get_image_src(self, obj: Breed) -> str | None:
        if obj.image:
            request = self.context.get("request")

            if request:
                return request.build_absolute_uri(obj.image.url)

            return obj.image.url

        return obj.image_url

    def get_traits(self, obj: Breed) -> dict[str, dict[str, Any]]:
        return {
            "size": {
                "label": "Розмір",
                "value": obj.size,
                "max": 3,
                "display": obj.get_size_display(),
            },
            "energy": {
                "label": "Рівень активності",
                "value": obj.energy,
                "max": 5,
                "display": obj.get_energy_display(),
            },
            "grooming": {
                "label": "Складність догляду",
                "value": obj.grooming,
                "max": 5,
                "display": obj.get_grooming_display(),
            },
            "kids_friendly": {
                "label": "Підходить для сімей з дітьми",
                "value": obj.kids_friendly,
                "max": 5,
                "display": obj.get_kids_friendly_display(),
            },
        }

    def get_housing(self, obj: Breed) -> list[str]:
        if obj.housing_type == Breed.HousingType.APARTMENT:
            return ["apartment"]

        if obj.housing_type == Breed.HousingType.HOUSE:
            return ["house"]

        return ["apartment", "house"]


class BreedComparisonSerializer(serializers.Serializer):
    first_breed = BreedCompareCardSerializer()
    second_breed = BreedCompareCardSerializer()
    conclusion = serializers.CharField()


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
