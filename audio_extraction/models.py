from django.db import models


class AudioExtraction(models.Model):
	# name = models.CharField(max_length=200)
	# timestamp = models.DateTimeField(auto_now_add=True)
	video = models.FileField(upload_to="audio_extraction/", null=True, default=None)
	extraction_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f"Audio from {self.video} extracted on {self.extraction_date}"