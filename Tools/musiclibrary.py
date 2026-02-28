import webbrowser
from ytmusicapi import YTMusic

# Initialize YTMusic (Unauthenticated is enough for basic searching)
yt = YTMusic()

def play_song(song_name):
    try:
        # 1. Search for the song
        # We filter by 'songs' to get direct music tracks instead of videos
        search_results = yt.search(song_name, filter="songs", limit=1)
        
        if search_results:
            video_id = search_results[0]['videoId']
            url = f"https://music.youtube.com/watch?v={video_id}"
            
            # 2. Open in default browser
            # For a "Hero" project, this is the most reliable playback method
            webbrowser.open(url)
            return f"Playing {search_results[0]['title']} on YouTube Music."
        else:
            return "Sorry, I couldn't find that song."
            
    except Exception as e:
        print(f"YT Music Error: {e}")
        return "There was an error accessing YouTube Music."