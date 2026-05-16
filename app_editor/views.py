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
        data = json.loads(request.body)
        file = data.get('file')
        duration = 0
        try:
            duration = mpy.VideoFileClip(f"{media_root}/{file}").duration
        except:
            duration = mpy.AudioFileClip(f"{media_root}/{file}").duration
        print(duration, "\nFile is: ", os.listdir(media_root), f"\nFile is {file}" )
        return render(request, 'app_editor/partials/time-section.html', {"dir": os.listdir(media_root), "duration": duration})
        # return HttpResponse("Good and good")
    return render(request, 'app_editor/home.html', {"dir": os.listdir(media_root)})


@csrf_exempt
def get_duration(request):
    if request.method == 'POST':
        # return JsonResponse(
        #     {"duration": 123}
        # )

        data = json.loads(request.body)
        file = data.get('file')
        try:
            return JsonResponse(
                {"duration": mpy.VideoFileClip(f"{media_root}/{file}").duration}
            )
        except:
            return JsonResponse(
                {"duration": mpy.AudioFileClip(f"{media_root}/{file}").duration}
            )
    if request.method == 'GET':
        return HttpResponse("Success GET request received")