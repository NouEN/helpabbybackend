from rest_framework import generics
from helpabbyapi.models import Food
from .serializers import FoodSerializer

class ListFoodAPI(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer