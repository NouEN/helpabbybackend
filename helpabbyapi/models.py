from django.db import models

# Create your models here.
class Myth(models.Model):
    mythDesc = models.CharField(max_length=1000)
    factDesc = models.CharField(max_length=1000)
    source = models.CharField(max_length=100)

class Food(models.Model):
    foodName = models.CharField(max_length=1000)
    calories = models.IntegerField()
    carbs = models.DecimalField(max_digits=1000, decimal_places=1)
    protein = models.DecimalField(max_digits=1000, decimal_places=1)
    fat = models.DecimalField(max_digits=1000, decimal_places=1)