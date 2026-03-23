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
