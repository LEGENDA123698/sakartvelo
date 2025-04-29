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
        return ResultSolution.objects.filter(user=self.request.user, is_active=False)


class OrderDetailView(DetailView):
    model = ResultSolution
    template_name = "get_order_app/detail_order.html"
    context_object_name = "order"


class OrderDeleteView(DeleteView):
    model = ResultSolution
    template_name = "get_order_app/delete_order.html"
    success_url = reverse_lazy("order-list")



# страница оформления заказа, формирует итоговую сумму и список блюд.
@login_required
def order_page(request):
    user = request.user

    # Получаем активные позиции корзины
    order_items = OrderItem.objects.filter(order__user=user, order__is_active=True)
    total_price = sum(float(item.dish.price) * item.quantity for item in order_items)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Удаляем все активные заказы пользователя
            ResultSolution.objects.filter(user=user, is_active=True).delete()

            # Создаем новый заказ
            order = ResultSolution.objects.create(
                user=user,
                comment=form.cleaned_data['comment'],
                delivery_date=form.cleaned_data['delivery_date'],
                delivery_time=form.cleaned_data['delivery_time'],
                total_price=total_price,
                is_active=False  # Заказ завершен
            )

            # Привязываем позиции к новому заказу
            for item in order_items:
                item.order = order
                item.save()

            # Удаляем временные (неоформленные) записи
            OrderItem.objects.filter(order__user=user, order__is_active=True).delete()

            return redirect('list-dish')
    else:
        form = OrderForm()

    context = {
        'order_items': order_items,
        'total_price': total_price,
        'form': form,
    }
    return render(request, 'get_order_app/order_form.html', context)

# Страница управления улицами
@login_required
def street_list(request):
    streets = Street.objects.all()
    form = StreetForm()
    return render(request, 'get_order_app/street_list.html', {'streets': streets, 'form': form})

# Добавление и удаление улицы
@login_required
def manage_street(request):
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

#добавление блюдо в корзину или создание его
def add_to_order(request, pk):
    dish = get_object_or_404(Dishes, pk=pk)

    quantity = request.POST.get('quantity', '1')
    try:
        quantity = int(quantity)
    except ValueError:
        return JsonResponse({'error': 'Некорректное количество'}, status=400)

    user = request.user
    order, _ = ResultSolution.objects.get_or_create(user=user, is_active=True)

    # Ищем уже существующую позицию в заказе
    order_item = OrderItem.objects.filter(user=user, dish=dish, order=order).first()

    if order_item:
        print(f"Перед изменением: ID {order_item.id}, количество {order_item.quantity}, добавляется {quantity}")
        order_item.quantity += quantity
    else:
        order_item = OrderItem.objects.create(
            user=user, dish=dish, order=order, quantity=quantity
        )
        print(f"Создан новый OrderItem: ID {order_item.id}, количество {order_item.quantity}")

    order_item.save()

    # Подсчитываем новую сумму
    total_price = sum(float(item.dish.price) * item.quantity for item in OrderItem.objects.filter(order=order))

    print(f"После изменения: ID {order_item.id}, новое количество {order_item.quantity}, Итоговая цена: {total_price}")

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'total_items': order_item.quantity, 'total_price': total_price})

    return redirect('detail-dish', pk=dish.pk)


# настройки вывода улиц
def street_suggestions(request):
    query = request.GET.get("query", "").strip().lower()
    
    if query:
        streets = Street.objects.filter(name__icontains=query)  # Фильтрация по вводу
    else:
        streets = Street.objects.all()  # Возвращаем весь список, если запроса нет
    
    street_list = list(streets.values_list("name", flat=True))  # Преобразуем в список строк
    return JsonResponse({"streets": street_list})


# Функция для изменения количества блюд в корзине
def update_item(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id)
    
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "increase":
            item.quantity += 1
        elif action == "decrease" and item.quantity > 1:
            item.quantity -= 1
        item.save()

        # Фильтруем только активный заказ пользователя
        active_order = ResultSolution.objects.filter(user=request.user, is_active=True).first()
        order_items = OrderItem.objects.filter(order=active_order)#!!!!
        total_price = sum(float(order_item.dish.price) * order_item.quantity for order_item in order_items)

        return JsonResponse({'success': True, 'new_quantity': item.quantity, 'total_price': total_price})

    
#отображение корзины с текущими позициями и итоговой ценой
def card_view(request):
    order_items = OrderItem.objects.filter(order__user=request.user)
    total_price = sum(item.dish.price * item.quantity for item in order_items)
    
    context = {
        "order_items": order_items,
        "total_price": total_price,
    }
    return render(request, "order_form.html", context)


def delete_order_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(OrderItem, id=item_id)
        order = item.order
        item.delete()

        # Обновляем общую сумму корзины для активного заказа
        order_items = OrderItem.objects.filter(order=order)
        total_price = sum(float(item.dish.price) * item.quantity for item in order_items)

        return JsonResponse({'success': True, 'total_price': total_price})
    
    return JsonResponse({'success': False, 'error': 'Неверный запрос'}, status=400)
