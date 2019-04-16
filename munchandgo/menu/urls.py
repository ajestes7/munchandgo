from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', views.RestaurantListView.as_view(), name='restaurants'),
    path('restaurant/<int:pk>', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('food/', views.FoodListView.as_view(), name='food'),
    path('food/<int:pk>', views.FoodDetailView.as_view(), name='food-detail'),
]
