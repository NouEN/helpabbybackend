from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Food, Myth
from .api.serializers import FoodSerializer, MythSerializer

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
    try:
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
    except Exception as e :
        Response({'status': 'ERROR', 'message': 'The error is ' + e})

@api_view(['GET'])
def getMythlist(request):
    try:
        myths = Myth.objects.all()
        serializer = MythSerializer(myths, many=True)
        return Response(serializer.data)
    except Exception as e :
        Response({'status': 'ERROR', 'message': 'The error is ' + e})