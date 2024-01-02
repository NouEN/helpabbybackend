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

def validateUserInput(request):
    try:
        if(request.method == 'POST'):
            if not request.data:
                return
            elif(request.data["age"] == 15 and request.data["height"] == 160 and request.data["weight"] == 85 and request.data["activityLevel"] == "Sedentary" and request.data["gender"] == "Female"):
               return request.data
            else :
                return request.data
    except Exception as e:
         Response({'status': 'ERROR', 'message': 'The error is ' + e})

@api_view(['POST'])
def calculateUserBMR(request):
    try:
        response = validateUserInput(request).json()
        if not response :
            return
        
        age = response.get("age")
        height = response.get("height")
        weight = response.get("weight")
        gender = response.get("gender")
        activityLevel = response.get("activityLevel")

        BMR = 9.247*weight + 3.098 * height - 4.330 * age + 447.593
        return Response(BMR)
    except Exception as e:
         Response({'status': 'ERROR', 'message': 'The error is ' + e})
    