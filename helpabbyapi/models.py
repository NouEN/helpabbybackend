from django.db import models
from django import forms

# Create your models here.
class Myth(models.Model):
    mythDesc = models.CharField(max_length=1000)
    factDesc = models.CharField(max_length=1000)
    source = models.CharField(max_length=1000)

class Food(models.Model):
    foodName = models.CharField(max_length=1000)
    calories = models.IntegerField()
    carbs = models.DecimalField(max_digits=1000, decimal_places=1)
    protein = models.DecimalField(max_digits=1000, decimal_places=1)
    fat = models.DecimalField(max_digits=1000, decimal_places=1)

# class Calculator(forms.Form):
#     age = forms.IntegerField(initial = 'age')
#     gender = forms.CharField(initial='gender', max_length='50')
#     height = forms.IntegerField(initial='height')
#     weight = forms.IntegerField(initial='weight')
#     activityLevel = forms.CharField(max_length=50, initial='activity level')  