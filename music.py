import os
from speak import speak
import random

# ===========================================
# Music
# ===========================================

def play_music():

    music_folder = r"C:\Users\sangr\OneDrive\Music"

    if not os.path.exists(music_folder):
        speak("Music folder not found.")
        return

    songs = []

    for file in os.listdir(music_folder):

        if file.lower().endswith((".mp3", ".wav")):
            songs.append(file)

    if len(songs) == 0:
        speak("No songs found.")
        return

    song = random.choice(songs)

    speak("Playing music")

    os.startfile(os.path.join(music_folder, song))
