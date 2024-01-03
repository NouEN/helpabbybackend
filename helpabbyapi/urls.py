from django.urls import path
from . import views
from helpabbyapi.api.api_views import ListFoodAPI

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('food/foodlist', views.getFoodlist),
    path('food/submit', views.calculateUserBMRandTDEE),
    path('myths/', views.getMythlist)
]