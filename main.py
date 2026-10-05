from unittest import skip


from speak import speak
from app import execute_command
import datetime
import speech_recognition as sr
recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.pause_threshold = 0.8
recognizer.dynamic_energy_threshold = True

def greet():
   hour = datetime.datetime.now().hour
   if hour < 12:
       speak("Good Morning, Hi Sangram,How can I help you today?")
   elif hour < 17:
       speak("Good Afternoon,Hi Sangram ,How can I help you today?")
   else:
       speak("Good Evening, Hi Sangram,How can I help you today?")


greet()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            # Adjust for ambient noise with the audio source passed in
            recognizer.adjust_for_ambient_noise(source, duration=10)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        # Transcribe audio using Google Speech Recognition
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        result = execute_command(command)
        if result is False:
            break

    except sr.UnknownValueError:
        print("Couldn't understand.")

    except sr.RequestError:
        speak("Speech Recognition service is unavailable.")

    except KeyboardInterrupt:
        speak("Goodbye.")
        break

    except Exception as e:
        print(e)


