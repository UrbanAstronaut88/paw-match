from rest_framework import generics
from .models import Breed
from .serializers import BreedSerializer


class BreedListView(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
