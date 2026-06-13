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
def home(request):
    return render(request, 'app_editor/home.html')


@csrf_exempt
def sundays(request):
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
    return render(request, 'app_editor/sundays.html', {"dir": os.listdir(media_root)})

@csrf_exempt
def process(request):
    # get data from frontend
    data = json.loads(request.body)
    wf =  data.get("working-file")
    duration = int(float(data.get("duration")))
    
    wf =  media_root + f"/{wf}"
    
    # load video/audio file
    clip = helpers.read_file(wf)

    # get time range dictionary
    time_dict = helpers.get_time_range(data, duration)

    # #process audio files
    if data.get("options-testimony") == 'audio' or data.get("options-testimony") == 'audiovideo':
        clip['audio'].subclipped(time_dict["testimony"][0] , 
                         time_dict["testimony"][1]
                         ).write_audiofile(f"{media_root}/output/{data.get("title-testimony")}.mp3")
        print("This should print first")
        
    if data.get("options-choir") == 'audio' or data.get("options-choir") == 'audiovideo':
        clip['audio'].subclipped(time_dict["choir"][0] , 
                         time_dict["choir"][1]
                         ).write_audiofile(f"{media_root}/output/{data.get("title-choir")}.mp3")

    if data.get("options-sermon") == 'audio' or data.get("options-sermon") == 'audiovideo':
        #make intro and outro speech
        # make intro_speech
        helpers.text_to_speech(data.get("intro"), f"{media_root}/assets/introspeech.mp3")

        # make outro_speech
        helpers.text_to_speech(data.get("outro"), f"{media_root}/assets/outrospeech.mp3")

        # subclip sermon audio
        sermon_subclip = clip['audio'].subclipped(time_dict["sermon"][0] , time_dict["sermon"][1])

        # Concatenate audio files and clips
        sermon_audio = helpers.concatenate_audios(sermon_subclip)
        
        sermon_audio.write_audiofile(f"{media_root}/output/{data.get("title-sermon")}.mp3")


    #process video files
    if data.get("options-testimony") == 'video' or data.get("options-testimony") == 'audiovideo':
        clip['video'].subclipped(time_dict["testimony"][0] , 
                         time_dict["testimony"][1]
                         ).write_videofile(f"{media_root}/output/{data.get("title-testimony")}.mp4")

    if data.get("options-choir") == 'video' or data.get("options-choir") == 'audiovideo':
        clip['video'].subclipped(time_dict["choir"][0] , 
                         time_dict["choir"][1]
                         ).write_videofile(f"{media_root}/output/{data.get("title-choir")}.mp4")

    if data.get("options-sermon") == 'video' or data.get("options-sermon") == 'audiovideo':
        clip['video'].subclipped(time_dict["sermon"][0] , 
                         time_dict["sermon"][1]
                         ).write_videofile(f"{media_root}/output/{data.get("title-sermon")}.mp4")
    
    # close read file
    helpers.close_clip(clip)
    print("\nThis should print second")

    return JsonResponse({"message": "Success"})

def compress(request):
    data = json.loads(request.body)
    file = data.get("file")
    name = file.split(".")[0]
    clip = helpers.read_file(f"{media_root}/{file}")
    if clip.type == 'audio':
        clip['audio'].write_audiofile(
            f"{media_root}/{name}_compressed.m4a",
            codec="aac",
            bitrate="64k"
        )
    if clip.type == 'video':
        clip['video'].write_videofile(
            f"{media_root}/{name}_compressed.mp4",
            codec="libx264",
            bitrate="500k"
        )

@csrf_exempt
def splice(request):
    if request.method == "POST":
        data = json.loads(request.body)
        time = data.get("time")
        file = data.get("file")
        name = file.split(".")[0]
        clip = helpers.read_file(f"{media_root}/{file}")
        try:
            clip_box = []
            if clip['type'] == 'audio':
                for t in time:
                    clip_box.append(
                        clip['audio'].subclipped(t['start'], t['end'])        
                    )
                mpy.concatenate_audioclips(clip_box).write_audiofile(
                    f"{media_root}/output/{name}_spliced.m4a",
                    codec="aac",
                    bitrate="64k"
                )
            if clip["type"] == 'video':
                for t in time:
                    clip_box.append(
                        clip['video'].subclipped(t['start'], t['end'])        
                    )
                mpy.concatenate_videoclips(clip_box).write_videofile(
                    f"{media_root}/output/{name}_spliced.mp4",
                    codec="libx264",
                    bitrate="500k"
                )
            return JsonResponse({'text': "File spliced successfuly!"})
        except Exception as e:
            return JsonResponse({'text': str(e)})

    return render(request, 'app_editor/splice.html', {"dir": os.listdir(media_root)})