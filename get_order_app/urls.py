from django.urls import path
from .views import *

urlpatterns = [
    path('order/', order_page, name='order-page'),
    path('add-to-order/<int:pk>/', add_to_order, name='add-to-order'),
    path('card/', card_view, name='card'),
    path('card/update-item/<int:item_id>/', update_item, name='update-item'),
    path('item/delete/<int:item_id>/', delete_order_item, name='order-item-delete'),
    path("streets/", street_list, name="street-list"),
    path("streets/manage/", manage_street, name="manage-street"),
    path('street-suggestions/', street_suggestions, name='street-suggestions'),
    path('profile/orders/', OrdersListView.as_view(), name="order-list"),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="delete-order"),
]