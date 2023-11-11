import os, uuid, shutil, subprocess
from tempfile import NamedTemporaryFile

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AudioExtraction


class AudioExtractionView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        video_file = request.data['video']
        video_filename = video_file.name

        # Create a temporary file for the uploaded video
        with NamedTemporaryFile(suffix='.mp4', delete=False) as temp_video:
            for chunk in video_file.chunks():
                temp_video.write(chunk)

        # Set the output file path for the audio
        output_file_destination = f"/audio_extraction/output/output_audio_{uuid.uuid4().hex}_{os.path.splitext(video_filename)[0]}.mp3"
        output_file = f"media/audio_extraction/output/output_audio_{uuid.uuid4().hex}_{os.path.splitext(video_filename)[0]}.mp3"

        # Command to extract audio using ffmpeg
        command = f'ffmpeg -i {temp_video.name} -vn -acodec libmp3lame {output_file}'

        try:
            subprocess.run(command, shell=True, check=True)
            if os.path.exists(output_file):
                audio_url = f"/{output_file}" 
                
                destination_folder = '/audio_extraction/input/'
                os.makedirs(destination_folder, exist_ok=True)
                shutil.copy(temp_video.name, destination_folder)
                audioextraction = AudioExtraction()
                audioextraction.video.name = destination_folder + temp_video.name.split('/')[-1]
                audioextraction.audio.name = output_file_destination
                audioextraction.save()
                return Response({'audio_url': audio_url}, status=200)
            else:
                return Response({'message': 'Audio extraction failed. No output file created.'}, status=400)
        except subprocess.CalledProcessError as e:
            return Response({'message': f'Audio extraction failed: {e.stderr}'}, status=400)