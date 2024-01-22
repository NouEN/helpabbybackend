from rest_framework import serializers
from helpabbyapi.models import Food,Myth

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields =  '__all__'

class MythSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myth
        fields =  '__all__'