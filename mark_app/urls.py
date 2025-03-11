from django.urls import path
from .views import *

urlpatterns = [
    path("submit-review/", submit_review, name="submit-review"),
    path("", home, name="main-page"),
    path("load_comments/", load_comments, name="load-comments"),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete-comment'),
]

