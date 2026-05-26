#helper functions defined here

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