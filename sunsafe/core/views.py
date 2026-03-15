from django.shortcuts import render

# Create your views here.
from django.db.models import Avg
from django.db.models.functions import ExtractYear
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView

from .models import UVIndexRecord
from .models import CancerYearlyStat

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
    

from .serializers import CancerYearlyStatSerializer

class CancerYearlyStatView(ListAPIView):
    serializer_class = CancerYearlyStatSerializer

    def get_queryset(self):
        qs = CancerYearlyStat.objects.all()

        region = self.request.query_params.get("region")
        cancer_type = self.request.query_params.get("cancer_type")

        if region:
            region = region.lower()
            if region == "australia":
                qs = qs.filter(region="Australia")
            elif region == "victoria":
                qs = qs.filter(region="Victoria")

        if cancer_type:
            qs = qs.filter(cancer_type=cancer_type)

        return qs.order_by("year")

