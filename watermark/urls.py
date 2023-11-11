from django.urls import path
from .views import WatermarkOverlayView


urlpatterns = [
    path("watermark-overlay/", WatermarkOverlayView.as_view(), name='watermark_overlay'),
]