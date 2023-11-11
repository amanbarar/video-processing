from rest_framework import serializers

class VideoUploadSerializer(serializers.Serializer):
    video = serializers.FileField()
    watermark = serializers.ImageField()
    position_x = serializers.IntegerField()
    position_y = serializers.IntegerField()
    