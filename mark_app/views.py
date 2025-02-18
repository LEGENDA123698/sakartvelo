from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from django.db.models import Avg

def submit_review(request):
    if request.method == "POST":
        user_reviews_count = Review.objects.filter(user=request.user).count()
        
        if user_reviews_count >= 3:
            messages.error(request, "Вы уже оставили 3 отзыва! Больше нельзя.")
            return redirect("main-page")

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, f"Ваш отзыв добавлен! Осталось попыток: {2 - user_reviews_count}")
            return redirect("main-page")
    else:
        form = ReviewForm()

    return render(request, "mark_app/mark_form.html", {"form": form})

def home(request):
    avg_dish_rating = Review.objects.aggregate(Avg("dish_rating"))["dish_rating__avg"] or 0
    avg_service_rating = Review.objects.aggregate(Avg("service_rating"))["service_rating__avg"] or 0

    return render(request, "main_html/main_screen.html", {
        "avg_dish_rating": avg_dish_rating,
        "avg_service_rating": avg_service_rating,
        "stars": range(1, 6),
    })
