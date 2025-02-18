from django.shortcuts import render
from django.views.generic import *
from mark_app.models import Review
from django.db.models import Avg

class MainView(TemplateView):
    template_name = "main_html/main_screen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        avg_dish_rating = Review.objects.aggregate(Avg("dish_rating"))["dish_rating__avg"] or 0
        avg_service_rating = Review.objects.aggregate(Avg("service_rating"))["service_rating__avg"] or 0

        context["avg_dish_rating"] = round(avg_dish_rating, 1)
        context["avg_service_rating"] = round(avg_service_rating, 1)

        context["stars"] = range(1, 6)

        return context
