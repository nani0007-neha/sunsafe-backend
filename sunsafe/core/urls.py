from django.urls import path
from .views import UvTrendView, CancerYearlyStatView

urlpatterns = [
    path("uv-trends/", UvTrendView.as_view(), name="uv-trends"),
    path("cancer-stats/", CancerYearlyStatView.as_view(), name="cancer-stats"),
]
