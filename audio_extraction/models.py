from django.db import models


class AudioExtraction(models.Model):
	video = models.FileField(upload_to="audio_extraction/input/", null=True, default=None)
	audio = models.FileField(upload_to="audio_extraction/output/", null=True, default=None)
	extraction_timestamp = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f"Audio from {self.video} extracted on {self.extraction_timestamp}"