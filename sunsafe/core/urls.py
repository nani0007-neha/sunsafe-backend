from django.urls import path
from .views import UvTrendView

urlpatterns = [
    path("uv-trends/", UvTrendView.as_view(), name="uv-trends"),
]
