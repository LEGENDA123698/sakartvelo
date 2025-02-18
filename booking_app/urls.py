from django.urls import path
from .views import *

urlpatterns = [
    path('booking/', BookingCreateView.as_view(), name='booking'),
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking-delete'),
    path('booking_list_for_choice/', BookingListForChoiceView.as_view(), name='booking-list-for-choice'),
]