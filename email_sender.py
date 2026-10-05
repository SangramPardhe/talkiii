# ===========================================
# AI Email Writer
# ===========================================

from speak import speak
import speech_recognition as sr
recognizer = sr.Recognizer()
from gemini import ask_ai







def write_email():

    speak("What should the email be about?")

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        prompt = recognizer.recognize_google(audio)

        speak("Writing your email.")

        email = ask_ai(
            f"Write a professional email about {prompt}"
        )

        print("\n========== EMAIL ==========\n")
        print(email)

        with open("email.txt", "w", encoding="utf-8") as file:
            file.write(email)

        speak("Email saved successfully.")

    except Exception:

        speak("Sorry, I couldn't generate the email.")

