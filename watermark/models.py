from django.db import models

class Watermark(models.Model):
    image = models.ImageField(upload_to='watermark/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class WatermarkedVideos(models.Model):
    watermark = models.ForeignKey(Watermark, on_delete=models.CASCADE)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)
    processed_video = models.FileField(upload_to='watermark/processed_video/', null=True, default=None)
    extraction_timestamp = models.DateTimeField(auto_now_add=True)
