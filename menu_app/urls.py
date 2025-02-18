from django.urls import path
from .views import *

urlpatterns = [
    path('', DishListView.as_view(), name='list-dish'),
    path('create/', DishCreateView.as_view(), name='create-dish'),
    path('<int:pk>/', DishDetailView.as_view(), name='detail-dish'),
    path('<int:pk>/update/', DishUpdateView.as_view(), name='update-dish'),
    path('<int:pk>/delete/', DishDeleteView.as_view(), name='delete-dish'),
    
    path('api/dishes/', DishesListAPI.as_view(), name='dishes-list-api'),
    path('api/dishes/<int:pk>', DishesDetailAPI.as_view(), name='dishes-detail-api'),
]
