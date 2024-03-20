from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Food, Myth
from .api.serializers import FoodSerializer, MythSerializer
import random
import json


@api_view(['GET'])
def home_page(request):
    return render("main.tsx", "main.tsx")

@api_view(['GET'])
def food_page(request):
    return render()

@api_view(['GET'])
def getFoodlist(request):
    try:
        foods = Food.objects.all().order_by('foodName')
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
    except Exception as e :
        Response({'status': 'ERROR', 'message': 'The error is ' + e})

@api_view(['GET'])
def getMythlist(request):
    try:
        myths = Myth.objects.all().order_by('id')
        serializer = MythSerializer(myths, many=True)
        return Response(serializer.data)
    except Exception as e :
        Response({'status': 'ERROR', 'message': 'The error is ' + e})

def validateUserInput(request):
    try:
        print(request)
        if((int(request.data["age"]) and request.data["age"] < 0) or (int(request.data["height"]) and request.data["height"] < 0 )
           or (int(request.data["weight"]) and request.data["weight"] < 0)):
            return False
        else:
            return True
    except Exception as e:
         Response({'status': 'ERROR', 'message': 'The error is ' + str(e)})

@api_view(['POST'])
def calculateUserBMRandTDEE(request):
    try:
        response = validateUserInput(request)
        if(response == False):
            return Response({'status': 'ERROR', 'message': 'Wrong Input!'})
        elif(response == True):
            age = int(request.data.get("age"))
            height = int(request.data.get("height"))
            weight = int(request.data.get("weight"))
            gender = request.data.get("gender")
            activityLevel = request.data.get("activityLevel")
            if(gender == 'Female'):
                BMR = (7.38 * weight) + (607 * (height/100)) - (2.31 * age) + 43
            elif(gender == 'Male'):
                BMR = (9.65 * weight) + (573 * (height/100)) - (5.08 * age) + 260  

            if(activityLevel == 'Sedentary'):
                tdee = 1.2 * BMR
            elif(activityLevel == 'Lightly Active'):
                tdee = 1.375 * BMR
            elif(activityLevel == 'Moderately Active'):
                tdee = 1.55 * BMR
            elif(activityLevel == 'Very Active'):
                tdee = 1.725 * BMR
            return Response({'status': 'SUCCESS', 'tdee': round(tdee), 'bmr': round(BMR)})
    except Exception as e:
         Response({'status': 'ERROR', 'message': 'The error is'+ str(e)  })