from rest_framework import serializers
from .models import Breed, QuizResult, Favorite


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult
        fields = ("id", "size", "energy", "kids", "housing_type", "created_at")


class FavoriteSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()

    class Meta:
        model = Favorite
        fields = ("id", "breed")


class MatchRequestSerializer(serializers.Serializer):
    size = serializers.IntegerField(min_value=1, max_value=3)
    energy = serializers.IntegerField(min_value=1, max_value=5)
    kids = serializers.IntegerField(min_value=1, max_value=5)
    housing_type = serializers.ChoiceField(choices=Breed.HousingType.choices)
