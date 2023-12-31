from rest_framework import serializers
from helpabbyapi.models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields =  '__all__'