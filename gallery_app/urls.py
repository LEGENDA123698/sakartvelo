from django.urls import path
from .views import *

urlpatterns = [
    path("", ImageView.as_view(), name="gallery"),
    path("upload/", ImageUploadView.as_view(), name="upload-image"),
    path("delete/<int:pk>/", ImageDeleteView.as_view(), name="delete-image"),
]

