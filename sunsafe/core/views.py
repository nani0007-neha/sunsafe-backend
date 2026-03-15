from django.shortcuts import render

# Create your views here.
from django.db.models import Avg
from django.db.models.functions import ExtractYear
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UVIndexRecord

class UvTrendView(APIView):
    def get(self, request):
        qs = UVIndexRecord.objects.filter(location="Melbourne")

        qs = (
            qs.annotate(year=ExtractYear("timestamp"))
              .values("year")
              .annotate(avg_uv_index=Avg("uv_level_index"))
              .order_by("year")
        )

        data = list(qs)
        return Response(data, status=status.HTTP_200_OK)
