from django.urls import path
from choice_app.views import *

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='list-category'),
    path('categories/<int:category_id>/', CategoryDishListView.as_view(), name='dishes-category'),
    path('category/create/', DishCategoryCreateView.as_view(), name='create-category'),
    path('delete-category/<int:pk>/', DishCategoryDeleteView.as_view(), name='delete-category'),
    path('category_for_delete/', ListCategoryView.as_view(), name='list-category-for-delete'),
    path('update-category/<int:pk>/', DishCategoryUpdateView.as_view(), name='update-category'),
    
    path('table/<int:pk>/edit/', TableUpdateView.as_view(), name='table-edit'),
    path('table/<int:pk>/delete/', TableDeleteView.as_view(), name='table-delete'),
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event-edit'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('table/add/', TableCreateView.as_view(), name='table-add'),
    path('event/add/', EventCreateView.as_view(), name='event-add'),

]
