from rest_framework import serializers
from .models import Dishes

class DisheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = "__all__"