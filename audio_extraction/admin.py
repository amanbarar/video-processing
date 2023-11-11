from django.contrib import admin

from .models import AudioExtraction

@admin.register(AudioExtraction)
class AudioExtractionAdmin(admin.ModelAdmin):
    list_display = ('id', 'video', 'audio', 'extraction_timestamp')
    search_fields = ('video', 'audio')  
    readonly_fields = ('id', 'extraction_timestamp',)
