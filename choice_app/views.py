from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import *
from .models import *
from menu_app.models import Dishes
from django.urls import reverse_lazy
from .forms import DishCategoryForm

class CategoryListView(ListView):
    model = Dish_Category
    template_name = 'categories/list_categories_in_dishes.html'
    context_object_name = 'categories' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Dish_Category.objects.all()
        print(context['categories'], "hello")
        return context


class CategoryDishListView(ListView):
    model = Dishes
    template_name = 'categories/dishe_category.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        category = Dish_Category.objects.get(id=category_id)
        print(category)
        return Dishes.objects.filter(choice=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Dish_Category.objects.all() 
        context['category'] = get_object_or_404(Dish_Category, id=self.kwargs.get('category_id'))
        return context
    
    
class DishCategoryCreateView(CreateView):
    model = Dish_Category
    form_class = DishCategoryForm
    template_name = 'categories/create_category.html'
    success_url = reverse_lazy('list-dish')
    
    
class DishCategoryDeleteView(DeleteView):
    model = Dish_Category
    template_name = 'categories/delete_category.html'
    success_url = reverse_lazy('list-category-for-delete')
    
class ListCategoryView(ListView):
    model = Dish_Category
    template_name = 'categories/list_category.html'
    context_object_name = 'categories'
    
    
class DishCategoryUpdateView(UpdateView):
    model = Dish_Category
    form_class = DishCategoryForm
    template_name = 'categories/update_category.html'
    success_url = reverse_lazy('list-category-for-delete')
    
    
    
class TableUpdateView(UpdateView):
    model = Table_Category
    fields = ['number']
    template_name = 'choice/table_edit.html'
    success_url = reverse_lazy('booking-list-for-choice')

class TableDeleteView(DeleteView):
    model = Table_Category
    template_name = 'choice/table_delete.html'
    success_url = reverse_lazy('booking-list-for-choice')

class EventUpdateView(UpdateView):
    model = Event_Category
    fields = ['event']
    template_name = 'choice/event_edit.html'
    success_url = reverse_lazy('booking-list-for-choice')

class EventDeleteView(DeleteView):
    model = Event_Category
    template_name = 'choice/event_delete.html'
    success_url = reverse_lazy('booking-list-for-choice')
    
class TableCreateView(CreateView):
    model = Table_Category
    fields = ['number']
    template_name = 'choice/table_add.html'
    success_url = reverse_lazy('booking-list-for-choice')

class EventCreateView(CreateView):
    model = Event_Category
    fields = ['event']
    template_name = 'choice/event_add.html'
    success_url = reverse_lazy('booking-list-for-choice')
    
