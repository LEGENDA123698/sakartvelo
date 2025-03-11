from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import BookingForm

from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Booking_Table
from .forms import BookingForm

class BookingCreateView(CreateView):
    model = Booking_Table
    form_class = BookingForm
    template_name = 'booking_app/booking_form.html'
    success_url = reverse_lazy('list-dish')

    def form_valid(self, form):
        table = form.cleaned_data['choice_table']
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']

        # Проверка, есть ли бронирование на этот столик в это время
        if Booking_Table.objects.filter(choice_table=table, date=date, time=time).exists():
            messages.error(self.request, "❌ Этот столик уже забронирован на указанное время.")
            return self.form_invalid(form)  # Обновит страницу и покажет ошибку

        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "✅ Бронирование успешно создано!")
        return response


    
class BookingListView(ListView):
    model = Booking_Table
    template_name = 'booking_app/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Booking_Table.objects.filter(user=self.request.user)
        return Booking_Table.objects.none()

class BookingDetailView(DetailView):
    model = Booking_Table
    template_name = 'booking_app/booking_detail.html'
    context_object_name = 'booking'

class BookingDeleteView(DeleteView):
    model = Booking_Table
    template_name = 'booking_app/booking_delete.html'
    success_url = reverse_lazy('booking-list')
    
    
class BookingListForChoiceView(ListView):
    model = Booking_Table
    template_name = 'booking_app/booking_list_for_choice.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking_Table.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booked_table = Booking_Table.objects.values_list('choice_table', flat=True)
        context['tables'] = Table_Category.objects.exclude(id__in=booked_table)
        context['events'] = Event_Category.objects.all()
        return context