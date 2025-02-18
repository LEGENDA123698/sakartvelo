from django.views.generic import *
from django.urls import reverse_lazy
from .models import Dishes
from choice_app.models import *
from .forms import DishForm
from rest_framework import generics
from .serializers import DisheSerializer


class DishesListAPI(generics.ListCreateAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DisheSerializer


class DishesDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DisheSerializer

class DishListView(ListView):
    model = Dishes
    template_name = 'dishes/list_dish.html'
    context_object_name = 'dishes'
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Dish_Category.objects.all()
        print(context['categories'], "hello")
        return context
    
    
class DishDetailView(DetailView):
    model = Dishes
    template_name = 'dishes/detail_dish.html'
    context_object_name = 'dish'


class DishCreateView(CreateView):
    model = Dishes
    form_class = DishForm
    template_name = 'dishes/create_dish.html'
    success_url = reverse_lazy('list-dish')


class DishUpdateView(UpdateView):
    model = Dishes
    form_class = DishForm
    template_name = 'dishes/update_dish.html'
    
    def get_success_url(self):
        return reverse_lazy('detail-dish', kwargs={'pk': self.object.pk})  


class DishDeleteView(DeleteView):
    model = Dishes
    template_name = 'dishes/delete_dish.html'
    success_url = reverse_lazy('list-dish')
    