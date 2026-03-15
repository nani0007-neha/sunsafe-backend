# your_app_name/serializers.py
from rest_framework import serializers
from .models import UVIndexRecord

class UVIndexRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UVIndexRecord
        fields = ["location", "uv_level_index", "timestamp"]
