# serializers.py
from rest_framework import serializers
from .models import AudioExtraction

class AudioExtractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioExtraction
        fields = ('video',)
