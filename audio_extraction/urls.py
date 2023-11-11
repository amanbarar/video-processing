from django.urls import path
from .views import AudioExtractionView, forms


urlpatterns = [
    path("home/", forms),
    # path("", AudioExtractionView.as_view()),
    path("audio-extract/", AudioExtractionView.as_view(), name='audio_extract'),
]