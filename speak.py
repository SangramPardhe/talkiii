import speech_recognition as sr

recognizer = sr.Recognizer()
# ===========================================
# Text To Speech
# ===========================================

import asyncio
import os
import pygame
import tempfile
import uuid
import edge_tts

def speak(text):
    text = str(text)
    print("Talkii:", text)

    async def generate():
        # Create a unique filename every time
        temp_file = os.path.join(
            tempfile.gettempdir(),
            f"talkii_{uuid.uuid4().hex}.mp3"
        )

        communicate = edge_tts.Communicate(
            text=text,
            voice="en-IN-NeerjaNeural"
        )

        await communicate.save(temp_file)

        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)

        pygame.mixer.music.unload()
        os.remove(temp_file)

    asyncio.run(generate())