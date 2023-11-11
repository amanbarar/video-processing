from django.urls import path
from .views import AudioExtractionView


urlpatterns = [
    path("audio-extract/", AudioExtractionView.as_view(), name='audio_extract'),
]