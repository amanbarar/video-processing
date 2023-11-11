from django.contrib import admin

from .models import AudioExtraction

# class AudioExtractionAdmin(admin.ModelAdmin):
#   list_display = ("name", "timestamp")

admin.site.register(AudioExtraction)