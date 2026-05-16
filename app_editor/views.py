from django.shortcuts import render
import os
import moviepy as mpy

import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


#variables 
# constants
media_root = "./media"

# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'POST':
        # receive the file name from the frontend and return the duration of the file
        data = json.loads(request.body)
        file = data.get('file')

        # get duration
        try:
            duration = mpy.VideoFileClip(f"{media_root}/{file}").duration
        except:
            duration = mpy.AudioFileClip(f"{media_root}/{file}").duration
        
        # determine which partial to return based on the duration of the file
        time_partial_dict = {
            60 : 'app_editor/partials/time-section60.html',
            3600 : 'app_editor/partials/time-section3600.html',
            7200: 'app_editor/partials/time-section7200.html',
        }
        if duration < 60:
            partial = time_partial_dict[60]
        elif duration < 3600:
            partial = time_partial_dict[3600]
        else:
            partial = time_partial_dict[7200]

        # return partial
        return render(request, partial, {"duration": duration})
    return render(request, 'app_editor/home.html', {"dir": os.listdir(media_root)})

