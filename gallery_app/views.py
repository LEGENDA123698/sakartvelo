from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from .models import Image
from .forms import ImageForm

class ImageView(ListView):
    model = Image
    template_name = "gallery_app/gallery.html"
    context_object_name = "images"



class ImageUploadView(SuccessMessageMixin, CreateView):
    model = Image
    form_class = ImageForm
    template_name = "gallery_app/image_form.html"
    success_url = reverse_lazy("gallery")
    success_message = "Фото успешно добавлено!"



class ImageDeleteView(DeleteView):
    model = Image
    success_url = reverse_lazy("gallery")

    def get(self, request, *args, **kwargs):
        """Перенаправляем на галерею при попытке открыть страницу удаления"""
        return self.post(request, *args, **kwargs)


