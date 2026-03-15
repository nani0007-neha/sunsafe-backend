# your_app_name/serializers.py
from rest_framework import serializers
from .models import UVIndexRecord
from .models import CancerYearlyStat

class UVIndexRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UVIndexRecord
        fields = ["location", "uv_level_index", "timestamp"]


class CancerYearlyStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancerYearlyStat
        fields = ["year", "region", "cancer_type", "cases"]