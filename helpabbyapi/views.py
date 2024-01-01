from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

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

@api_view(['GET','POST'])
def validateUserInput(request):
    try:
        if(request.method == 'POST'):
            if(request.data["age"] == 15 and request.data["height"] == 160 and request.data["weight"] == 85 and request.data["activityLevel"] == "Sedentary" and request.data["gender"] == "Female"):
               return Response(request.data)
            else :
                return Response()
    except Exception as e:
         Response({'status': 'ERROR', 'message': 'The error is ' + e})

@api_view(['POST'])
def calculateUserBMR(request):
    response = validateUserInput(request)
    
    