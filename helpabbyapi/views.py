from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Food
from .api.serializers import FoodSerializer

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['GET'])
def home_page(request):
    return render("main.tsx", "main.tsx")

@api_view(['GET'])
def food_page(request):
    return render()

@api_view(['GET'])
def getFoodlist(request):
    if(request.method == 'GET'):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
    return Response({'status': 'ERROR', 'message': 'Error to fetch all food data!'})