from rest_framework import generics
from django.shortcuts import render
from django.views.generic import ListView

from .models import AudioExtraction
from .serializers import AudioExtractionSerializer

def forms(request):
    video = AudioExtraction.objects.all()
    return render(request, "forms.html", {"video" : video})

# def AudioExtractionListView(ListView):
#     model = AudioExtraction
#     template_name = 'audio_extraction_list.html'


# class AudioExtractionView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         video_file = request.data['video']

#         # Save the in-memory uploaded file to a temporary file
#         with NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
#             for chunk in video_file.chunks():
#                 temp_file.write(chunk)

#         # Extract audio from the temporary file using ffmpeg-python
#         input_file = temp_file.name
#         output_file = 'output_audio.mp3'  # Replace with your desired output file name/path

#         ffmpeg.input(input_file).output(output_file).run()

#         # Serve the audio file for download
#         with open(output_file, 'rb') as audio:
#             response = Response(audio, content_type='audio/mpeg')
#             response['Content-Disposition'] = 'attachment; filename="extracted_audio.mp3"'
#             return response

import subprocess
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from tempfile import NamedTemporaryFile
from django.http import FileResponse
import os

import subprocess
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from tempfile import NamedTemporaryFile
from django.http import FileResponse
import os

class AudioExtractionView(APIView):
    import subprocess
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from tempfile import NamedTemporaryFile
from django.http import FileResponse
from django.conf import settings
import os, uuid

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
        output_file = f"output_audio_{uuid.uuid4().hex}_{os.path.splitext(video_filename)[0]}.mp3"

        # Command to extract audio using ffmpeg
        command = f'ffmpeg -i {temp_video.name} -vn -acodec libmp3lame {output_file}'

        try:
            subprocess.run(command, shell=True, check=True)
            if os.path.exists(output_file):
                audio_url = f"{settings.MEDIA_URL}{output_file}" 
                return Response({'audio_url': audio_url}, status=200)
            else:
                return Response({'message': 'Audio extraction failed. No output file created.'}, status=400)
        except subprocess.CalledProcessError as e:
            return Response({'message': f'Audio extraction failed: {e.stderr}'}, status=400)
