from rest_framework import serializers
from .models import CareAndHealthModel, PetsModel


class CareAndHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareAndHealthModel
        fields = ['id', 'description', 'title', 'image_url']


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetsModel
        fields = ['id', 'description', 'title', 'image_url']

