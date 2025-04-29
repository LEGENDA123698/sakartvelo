from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from django.db.models import Avg
from django.http import JsonResponse
from django.utils.timezone import localtime

def delete_comment(request, comment_id):
    if not request.user.is_staff:
        return JsonResponse({"error": "Ошибка!"}, status=403)

    comment = get_object_or_404(Review, id=comment_id)
    comment.delete()

    return JsonResponse({"success": True})

def load_comments(request):
    offset = int(request.GET.get("offset", 0))
    limit = 3  # Сколько загружаем за раз
    reviews = Review.objects.all().order_by("-created_at")[offset:offset+limit]

    data = {
        "comments": [
            {
                "id": review.id,
                "user": review.user.username,
                "dish_rating": review.dish_rating,
                "service_rating": review.service_rating,
                "comment": review.comment,
                "created_at": localtime(review.created_at).strftime("%Y-%m-%d %H:%M"),
                "is_staff": request.user.is_staff,
            }
            for review in reviews
        ],
        "has_more": Review.objects.count() > offset + limit,
        "total_count": Review.objects.count(),
    }

    return JsonResponse(data)

# обработка отправки отзыва от пользователя
def submit_review(request):
    if request.method == "POST":
        user_reviews_count = Review.objects.filter(user=request.user).count()
        
        if user_reviews_count >= 3:
            messages.error(request, "Ви вже залишили 3 відгуки! Більше не можна.")
            return redirect("main-page")

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, f"Ваш відгук додано! Залишилось спроб: {2 - user_reviews_count}")
            return redirect("main-page")
    else:
        form = ReviewForm()

    return render(request, "mark_app/mark_form.html", {"form": form})

# отображение элементов главной страницы(рейт,ком)
def home(request):
    avg_dish_rating = Review.objects.aggregate(Avg("dish_rating"))["dish_rating__avg"] or 0
    avg_service_rating = Review.objects.aggregate(Avg("service_rating"))["service_rating__avg"] or 0
    comments = Review.objects.all()[:3]
    total_comments = Review.objects.count()
    
    print("Total comments from DB:", Review.objects.count())

    return render(request, "main_html/main_screen.html", {
        "avg_dish_rating": avg_dish_rating,
        "avg_service_rating": avg_service_rating,
        "stars": range(1, 6),
        "comments": comments,
        "total_comments": total_comments
    })
