import webbrowser
from ytmusicapi import YTMusic

# Initialize YTMusic
yt = YTMusic()

def play_song(song_name):
    try:
        search_results = yt.search(song_name, filter="songs", limit=1)
        
        if search_results:
            video_id = search_results[0]['videoId']
            url = f"https://music.youtube.com/watch?v={video_id}"
            
            webbrowser.open(url)
            return f"Playing {search_results[0]['title']} on YouTube Music."
        else:
            return "Sorry, I couldn't find that song."
            
    except Exception as e:
        print(f"YT Music Error: {e}")
        return "There was an error accessing YouTube Music."