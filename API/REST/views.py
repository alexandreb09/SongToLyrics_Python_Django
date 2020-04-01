# Create your views here.
from django.http import JsonResponse

from rest_framework.decorators import api_view
from pydub import AudioSegment
import io

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from dejavu.parameters import config

import warnings
warnings.filterwarnings("ignore")

#################################################

#################################################

@api_view(['GET', 'POST'])
def mon_super_test(request):
    print("=" * 50)

    print(request.data)
    files = request.data.get("uploaded_file")

    # Read song from parameters -> download it as mp3 file    
    files.file.seek(0)
    b = io.BytesIO(files.file.read())
    song = AudioSegment.from_file(b, format="3gp")
    song.export("temp/test.mp3", format="mp3")

    # create a Dejavu instance
    djv = Dejavu(config)

    # Recognize audio from a file
    song_found = djv.recognize(FileRecognizer, "temp/test.mp3")


    if song_found: 
        song_name = song_found.get('song_name').split("--")
        artist = song_name[0]
        title = song_name[1]
    else: 
        artist = ""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        title = ""

    return JsonResponse({
        'artist': artist,
        'title': title
        })
