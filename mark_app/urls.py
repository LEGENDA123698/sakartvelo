from django.urls import path
from .views import *

urlpatterns = [
    path("submit-review/", submit_review, name="submit-review"),
    path("", home, name="main-page"),
]

