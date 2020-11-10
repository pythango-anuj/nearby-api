from rest_framework import serializers
from .models import Nearby

class Nearbyserializers(serializers.ModelSerializer):
    class Meta:
        model = Nearby
        fields = '__all__'
