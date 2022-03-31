from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.cars_list),
    path('<int:pk>/', views.car_detail),
]    