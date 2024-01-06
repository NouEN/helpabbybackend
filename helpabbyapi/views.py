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
        if(request.data["age"] == 15 and request.data["height"] == 160 and request.data["weight"] == 85 and request.data["activityLevel"] == "Sedentary" and request.data["gender"] == "Female"):
            return True
        else :
            return False
    except Exception as e:
         Response({'status': 'ERROR', 'message': 'The error is ' + str(e)})

@api_view(['POST'])
def calculateUserBMRandTDEE(request):
    try:
        response = validateUserInput(request)
        if(response == False):
            return Response({'status': 'ERROR', 'message': 'wrong input'})
        elif(response == True):
            age = int(request.data.get("age"))
            height = int(request.data.get("height"))
            weight = int(request.data.get("weight"))
            gender = request.data.get("gender")
            activityLevel = request.data.get("activityLevel")
            if(gender == 'Female'):
                BMR = 9.247 *weight + 3.098 * height - 4.330 * age + 447.593
            elif(gender == 'Male'):
                BMR = 13.397*weight + 4.799 * height - 5.677 * age + 88.362  

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
