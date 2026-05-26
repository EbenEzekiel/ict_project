from django.shortcuts import render
import os
import moviepy as mpy
from . import helpers

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
            duration = int(mpy.VideoFileClip(f"{media_root}/{file}").duration)
        except:
            duration = int(mpy.AudioFileClip(f"{media_root}/{file}").duration)
        
        # determine which partial to return based on the duration of the file
        partial = helpers.choose_partial(duration)

        # Convert time in seconds to Hr:min:sec format
        formatted_duration = helpers.format_seconds(duration)

        # return partial
        return render(request, partial, {"duration": duration, "formatted_duration" : formatted_duration})
    return render(request, 'app_editor/home.html', {"dir": os.listdir(media_root)})

@csrf_exempt
def process(request):
    # get data from frontend
    data = json.loads(request.body)
    wf =  data.get("working-file")
    duration = int(float(data.get("duration")))
    
    wf =  media_root + f"/{wf}"
    video = mpy.VideoFileClip(wf)
    
    # load video file
    video = mpy.VideoFileClip(wf)
    # get time range dictionary
    if duration < 60:
        time_dict = {
            "testimony": [f"{data.get("t1-sec-testimony")}", f"{data.get("t2-sec-testimony")}"],
            "choir": [f"{data.get("t1-sec-choir")}", f"{data.get("t2-sec-choir")}"],
            "sermon": [f"{data.get("t1-sec-sermon")}", f"{data.get("t2-sec-sermon")}"], 
        }
    elif duration < 3600:
        time_dict = {
            "testimony": [f"{data.get("t1-min-testimony")}:{data.get("t1-sec-testimony")}", 
                          f"{data.get("t2-min-testimony")}:{data.get("t2-sec-testimony")}"],

            "choir": [f"{data.get("t1-min-choir")}:{data.get("t1-sec-choir")}", 
                      f"{data.get("t2-min-choir")}:{data.get("t2-sec-choir")}"],

            "sermon": [f"{data.get("t1-min-sermon")}:{data.get("t1-sec-sermon")}",
                        f"{data.get("t2-min-sermon")}:{data.get("t2-sec-sermon")}"], 
        }
    else:
        time_dict = {
            "testimony": [f"{data.get("t1-hr-testimony")}:{data.get("t1-min-testimony")}:{data.get("t1-sec-testimony")}", 
                          f"{data.get("t2-hr-testimony")}:{data.get("t2-min-testimony")}:{data.get("t2-sec-testimony")}"],

            "choir": [f"{data.get("t1-hr-choir")}:{data.get("t1-min-choir")}:{data.get("t1-sec-choir")}", 
                      f"{data.get("t2-hr-choir")}:{data.get("t2-min-choir")}:{data.get("t2-sec-choir")}"],

            "sermon": [f"{data.get("t1-hr-sermon")}:{data.get("t1-min-sermon")}:{data.get("t1-sec-sermon")}",
                       f"{data.get("t2-hr-sermon")}:{data.get("t2-min-sermon")}:{data.get("t2-sec-sermon")}"], 
        }

    # #process audio files
    if data.get("options-testimony") == 'audio' or data.get("options-testimony") == 'audiovideo':
        video.subclipped(time_dict["testimony"][0] , 
                         time_dict["testimony"][1]
                         ).audio.write_audiofile(f"{media_root}/output/{data.get("title-testimony")}.mp3")

    if data.get("options-choir") == 'audio' or data.get("options-choir") == 'audiovideo':
        video.subclipped(time_dict["choir"][0] , 
                         time_dict["choir"][1]
                         ).audio.write_audiofile(f"{media_root}/output/{data.get("title-choir")}.mp3")

    if data.get("options-sermon") == 'audio' or data.get("options-sermon") == 'audiovideo':
        video.subclipped(time_dict["sermon"][0] , 
                         time_dict["sermon"][1]
                         ).audio.write_audiofile(f"{media_root}/output/{data.get("title-sermon")}.mp3")


    #process video files
    if data.get("options-testimony") == 'video' or data.get("options-testimony") == 'audiovideo':
        video.subclipped(time_dict["testimony"][0] , 
                         time_dict["testimony"][1]
                         ).write_videofile(f"{media_root}/output/{data.get("title-testimony")}.mp4")

    if data.get("options-choir") == 'video' or data.get("options-choir") == 'audiovideo':
        video.subclipped(time_dict["choir"][0] , 
                         time_dict["choir"][1]
                         ).write_videofile(f"{media_root}/output/{data.get("title-choir")}.mp4")

    if data.get("options-sermon") == 'video' or data.get("options-sermon") == 'audiovideo':
        video.subclipped(time_dict["sermon"][0] , 
                         time_dict["sermon"][1]
                         ).write_videofile(f"{media_root}/output/{data.get("title-sermon")}.mp4")

    return JsonResponse({"message": "Success"})