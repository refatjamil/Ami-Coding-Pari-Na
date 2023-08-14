from rest_framework import serializers
from .models import Khoj

class CustomDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        formatted_value = value.strftime('%Y-%m-%d %H:%M:%S')[:-3]
        return formatted_value

class KhojSerializer(serializers.ModelSerializer):
    timestamp = CustomDateTimeField()

    class Meta:
        model=Khoj
        fields = ['input_values', 'timestamp']

