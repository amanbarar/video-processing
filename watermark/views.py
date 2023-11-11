import os, uuid, subprocess, shutil
from tempfile import NamedTemporaryFile

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Watermark, WatermarkedVideos


class WatermarkOverlayView(APIView):

    def post(self, request, *args, **kwargs):
        video_file = request.data['video']
        video_filename = video_file.name
        watermark_file = request.data['watermark']
        position_x = request.data.get('position_x', '0')
        position_y = request.data.get('position_y', '0')

        with NamedTemporaryFile(suffix='.mp4', delete=False) as temp_video, NamedTemporaryFile(suffix='.png', delete=False) as temp_watermark:
            for chunk in video_file.chunks():
                temp_video.write(chunk)
            for chunk in watermark_file.chunks():
                temp_watermark.write(chunk)

        output_file = f"media/watermark/processed_video/output_video_{uuid.uuid4().hex}_{os.path.splitext(video_filename)[0]}.mp4"


        command = f'ffmpeg -i {temp_video.name} -i {temp_watermark.name} -filter_complex "overlay={position_x}:{position_y}" {output_file}'

        try:
            subprocess.run(command, shell=True, check=True)
            if os.path.exists(output_file):
                destination_folder = '/code/media/watermark/images/'
                os.makedirs(destination_folder, exist_ok=True)
                shutil.copy(temp_watermark.name, destination_folder)
                
                watermark = Watermark()
                watermark.image.name = destination_folder + temp_watermark.name.split('/')[-1]
                watermark.save()

                watermarkedvideos = WatermarkedVideos()
                watermarkedvideos.watermark = watermark
                watermarkedvideos.position_x, watermarkedvideos.position_y = position_x, position_y
                watermarkedvideos.save()

                return Response({'message': 'Watermark added successfully.', 'processed_video_url': f'/{output_file}'}, status=200)
            else:
                return Response({'message': 'Watermark addition failed. No output file created.'}, status=400)
        except subprocess.CalledProcessError as e:
            return Response({'message': f'Watermark addition failed: {e.stderr}'}, status=400)
