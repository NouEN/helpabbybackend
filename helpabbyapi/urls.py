from django.urls import path
from . import views
from helpabbyapi.api.api_views import ListFoodAPI

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('/', ListFoodAPI.as_view(), name='food_list')
]