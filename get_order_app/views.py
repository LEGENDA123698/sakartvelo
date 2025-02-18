from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import *
from menu_app.models import Dishes
from .forms import *
from django.views.generic import *
from django.contrib.auth.decorators import login_required
import requests
from django.urls import reverse_lazy

class OrdersListView(ListView):
    model = ResultSolution
    template_name = "get_order_app/list_orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        return ResultSolution.objects.filter(user=self.request.user)

class OrderDetailView(DetailView):
    model = ResultSolution
    template_name = "get_order_app/detail_order.html"
    context_object_name = "order"


class OrderDeleteView(DeleteView):
    """Позволяет пользователю удалить заказ"""
    model = ResultSolution
    template_name = "get_order_app/delete_order.html"
    success_url = reverse_lazy("order-list")


@login_required
def order_page(request):
    user = request.user
    order_items = OrderItem.objects.filter(order__user=user)
    total_price = sum(float(item.dish.price) * item.quantity for item in order_items)
    total_items = sum(item.quantity for item in order_items)  # Количество всех блюд

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = ResultSolution.objects.create(
                user=user,
                comment=form.cleaned_data['comment'],
                delivery_date=form.cleaned_data['delivery_date'],
                delivery_time=form.cleaned_data['delivery_time'],
                total_price=total_price,
            )
            for item in order_items:
                item.order = order
                item.save()
            OrderItem.objects.filter(order__user=user, order__isnull=True).delete()
            return redirect('list-dish')
    else:
        form = OrderForm()

    context = {
        'order_items': order_items,
        'total_price': total_price,
        'total_items': total_items,  # Передаем в шаблон
        'form': form,
    }
    return render(request, 'get_order_app/order_form.html', context)


@login_required
def street_list(request):
    """Страница управления улицами"""
    streets = Street.objects.all()
    form = StreetForm()
    return render(request, 'get_order_app/street_list.html', {'streets': streets, 'form': form})

@login_required
def manage_street(request):
    """Добавление и удаление улицы"""
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "add":
            form = StreetForm(request.POST)
            if form.is_valid():
                form.save()
        elif action == "delete":
            street_id = request.POST.get("street_id")
            Street.objects.filter(id=street_id).delete()
    
    return redirect("street-list")


def add_to_order(request, pk):
    dish = get_object_or_404(Dishes, pk=pk)
    quantity = int(request.POST.get('quantity', 1))
    user = request.user
    orders = ResultSolution.objects.filter(user=user, is_active=True)
    if orders.exists():
        order = orders.first()
    else:
        order = ResultSolution.objects.create(user=user, is_active=True)
    order_item, created = OrderItem.objects.get_or_create(order=order, dish=dish, user=user)
    if created:
        order_item.quantity = quantity
    else:
        order_item.quantity += quantity
    order_item.save()
    
    # Подсчитываем общее количество товаров в корзине
    total_items = sum(item.quantity for item in OrderItem.objects.filter(order__user=user))
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'total_items': total_items})
    
    return redirect('detail-dish', pk=dish.pk)



def street_suggestions(request):
    query = request.GET.get("query", "").strip().lower()
    
    if query:
        streets = Street.objects.filter(name__icontains=query)  # Фильтрация по вводу
    else:
        streets = Street.objects.all()  # Возвращаем весь список, если запроса нет
    
    street_list = list(streets.values_list("name", flat=True))  # Преобразуем в список строк
    return JsonResponse({"streets": street_list})


def update_item(request, item_id):
    """Функция для изменения количества блюд в корзине."""
    item = get_object_or_404(OrderItem, id=item_id)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "increase":
            item.quantity += 1
        elif action == "decrease" and item.quantity > 1:
            item.quantity -= 1
        item.save()

        # Подсчитываем новую общую сумму
        order_items = OrderItem.objects.filter(order__user=request.user)
        total_price = sum(float(item.dish.price) * item.quantity for item in order_items)

        return JsonResponse({'success': True, 'new_quantity': item.quantity, 'total_price': total_price})
    
    
def card_view(request):
    """Отображение корзины."""
    order_items = OrderItem.objects.filter(order__user=request.user)
    total_price = sum(item.dish.price * item.quantity for item in order_items)
    
    context = {
        "order_items": order_items,
        "total_price": total_price,
    }
    return render(request, "order_form.html", context)


def delete_order_item(request, item_id):
    """Удаление блюда из корзины."""
    if request.method == 'POST':
        item = get_object_or_404(OrderItem, id=item_id)
        item.delete()

        # Обновляем общую сумму корзины
        order_items = OrderItem.objects.filter(order__user=request.user)
        total_price = sum(float(item.dish.price) * item.quantity for item in order_items)

        return JsonResponse({'success': True, 'total_price': total_price})
    return JsonResponse({'success': False, 'error': 'Неверный запрос'}, status=400)