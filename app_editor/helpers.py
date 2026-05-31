#helper functions defined here
import pyttsx3
import moviepy as mpy

media_root = "./media"

def text_to_speech(text, filename):
    """this function converts text to speech and saves it as an mp3 file.
    It takes in the text to be converted and the filename for the output mp3 file."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)   # Speed of speech
    engine.setProperty('volume', 1.0) # Volume (0.0 to 1.0)
    engine.save_to_file(text, filename)
    engine.runAndWait()

    
def format_seconds(seconds):
    """this function formats time in seconds to the Hr:min:sec format.
    It takes in time value in seconds."""
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds} sec"
    elif seconds < 3600:
        min, sec = (seconds % 3600) // 60, seconds % 60
        return f"{min:02}min : {sec:02}sec"
    else:
        hr, min, sec = seconds // 3600, (seconds % 3600) // 60, seconds % 60
        return f"{hr}hr : {min:02}min : {sec:02}sec"
    
def choose_partial(seconds):
    time_partial_dict = {
            60 : 'app_editor/partials/time-section60.html',
            3600 : 'app_editor/partials/time-section3600.html',
            7200: 'app_editor/partials/time-section7200.html',
        }
    if seconds < 60:
        return time_partial_dict[60] 
    elif seconds < 3600:
        return time_partial_dict[3600]
    else:
        return time_partial_dict[7200]
    
def concatenate_audios(sermon_audio,):
    """this function concatenates the intros, sermon and outros audio files."""
    return mpy.concatenate_audioclips([
        mpy.AudioFileClip( f"{media_root}/assets/intro1.mp3"),
        mpy.AudioFileClip( f"{media_root}/assets/introspeech.mp3"),
        mpy.AudioFileClip( f"{media_root}/assets/intro2.mp3"),
        sermon_audio,
        mpy.AudioFileClip( f"{media_root}/assets/outro1.mp3"),
        mpy.AudioFileClip( f"{media_root}/assets/outrospeech.mp3"),
        mpy.AudioFileClip( f"{media_root}/assets/outro2.mp3"),
    ])

def get_time_range(data, duration):
    if duration < 60:
        return {
            "testimony": [f"{data.get("t1-sec-testimony")}", f"{data.get("t2-sec-testimony")}"],
            "choir": [f"{data.get("t1-sec-choir")}", f"{data.get("t2-sec-choir")}"],
            "sermon": [f"{data.get("t1-sec-sermon")}", f"{data.get("t2-sec-sermon")}"], 
        }
    elif duration < 3600:
        return {
            "testimony": [f"{data.get("t1-min-testimony")}:{data.get("t1-sec-testimony")}", 
                          f"{data.get("t2-min-testimony")}:{data.get("t2-sec-testimony")}"],

            "choir": [f"{data.get("t1-min-choir")}:{data.get("t1-sec-choir")}", 
                      f"{data.get("t2-min-choir")}:{data.get("t2-sec-choir")}"],

            "sermon": [f"{data.get("t1-min-sermon")}:{data.get("t1-sec-sermon")}",
                        f"{data.get("t2-min-sermon")}:{data.get("t2-sec-sermon")}"], 
        }
    else:
        return {
            "testimony": [f"{data.get("t1-hr-testimony")}:{data.get("t1-min-testimony")}:{data.get("t1-sec-testimony")}", 
                          f"{data.get("t2-hr-testimony")}:{data.get("t2-min-testimony")}:{data.get("t2-sec-testimony")}"],

            "choir": [f"{data.get("t1-hr-choir")}:{data.get("t1-min-choir")}:{data.get("t1-sec-choir")}", 
                      f"{data.get("t2-hr-choir")}:{data.get("t2-min-choir")}:{data.get("t2-sec-choir")}"],

            "sermon": [f"{data.get("t1-hr-sermon")}:{data.get("t1-min-sermon")}:{data.get("t1-sec-sermon")}",
                       f"{data.get("t2-hr-sermon")}:{data.get("t2-min-sermon")}:{data.get("t2-sec-sermon")}"], 
        }
