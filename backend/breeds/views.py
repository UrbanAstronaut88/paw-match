from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Breed
from .serializers import BreedSerializer
from .services.matching import get_best_matches



class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class MatchView(APIView):
    def post(self, request):

        user_data = request.data

        breeds = Breed.objects.all()

        matches = get_best_matches(user_data, breeds)

        result = []

        for item in matches:
            breed_data = BreedSerializer(item["breed"]).data
            breed_data["score"] = item["score"]
            result.append(breed_data)

        return Response(result, status=status.HTTP_200_OK)
