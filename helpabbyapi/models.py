from django.db import models
from django import forms

# Create your models here.
class Myth(models.Model):
    mythDesc = models.CharField(max_length=1000, unique=True)
    factDesc = models.CharField(max_length=1000)
    source = models.CharField(max_length=1000)

class Food(models.Model):
    foodName = models.CharField(max_length=1000, unique=True)
    calories = models.IntegerField()
    category = models.CharField(max_length=1000, default='N/A')
    carbs = models.DecimalField(max_digits=1000, decimal_places=1)
    protein = models.DecimalField(max_digits=1000, decimal_places=1)
    fat = models.DecimalField(max_digits=1000, decimal_places=1)
