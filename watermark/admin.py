from django.contrib import admin

from .models import Watermark, WatermarkedVideos


@admin.register(Watermark)
class WatermarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at')
    readonly_fields = ('uploaded_at',)

@admin.register(WatermarkedVideos)
class WatermarkedVideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'watermark', 'position_x', 'position_y', 'extraction_timestamp')
    readonly_fields = ('extraction_timestamp',)
