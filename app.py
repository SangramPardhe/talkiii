import webbrowser
import datetime
import subprocess
import os
from speak import speak
from music import play_music
from gemini import ask_ai
from email_sender import write_email

def open_camera():
    speak("Opening Camera")
    subprocess.run("start microsoft.windows.camera:")


def open_notepad():
    speak("Opening Notepad")
    subprocess.run("notepad")


def open_calculator():
    speak("Opening Calculator")
    subprocess.run("calc")


def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")


def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")


def tell_time():
    current = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current}")


def tell_date():
    today = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today is {today}")

# from here data commands and their functioned are available so ......



def open_powerbi():
    speak("Opening Power BI")
    os.startfile(r"C:\Users\Public\Desktop\Power BI Desktop.lnk")

def open_excel():
    speak("Opening Microsoft Excel")
    subprocess.run("start excel", shell=True)


def open_jupyter_notebook():
    speak("Opening Jupyter Notebook")
    subprocess.Popen("jupyter notebook", shell=True)


def open_anaconda():
    speak("Opening Anaconda Navigator")
    subprocess.Popen("anaconda-navigator", shell=True)

def open_vscode():
    speak("Opening Visual Studio Code")
    subprocess.run("code")


def open_mysql_workbench():
    speak("Opening MySQL Workbench")
    subprocess.run("start mysqlworkbench", shell=True)



def open_kaggle():
    speak("Opening Kaggle")
    webbrowser.open("https://www.kaggle.com")


def open_google_colab():
    speak("Opening Google Colab")
    webbrowser.open("https://colab.research.google.com")


def open_github():
    speak("Opening GitHub")
    webbrowser.open("https://github.com")


def open_pandas_docs():
    speak("Opening Pandas Documentation")
    webbrowser.open("https://pandas.pydata.org/docs/")


def open_numpy_docs():
    speak("Opening NumPy Documentation")
    webbrowser.open("https://numpy.org/doc/")


def open_matplotlib_docs():
    speak("Opening Matplotlib Documentation")
    webbrowser.open("https://matplotlib.org/stable/")


def open_seaborn_docs():
    speak("Opening Seaborn Documentation")
    webbrowser.open("https://seaborn.pydata.org/")


def open_scikit_docs():
    speak("Opening Scikit-Learn Documentation")
    webbrowser.open("https://scikit-learn.org/stable/")




def execute_command(command):

    if "open google" in command:
        open_google()
        return True

    elif "open youtube" in command:
        open_youtube()
        return True

    elif "open notepad" in command:
        open_notepad()
        return True

    elif "open calculator" in command:
        open_calculator()
        return True

    elif "play music" in command or "open music" in command:
        play_music()
        return True

    elif "time" in command:
        tell_time()
        return True

    elif "date" in command:
        tell_date()
        return True
    elif "email" in command or "write email" in command:
        write_email()
        return True
    #from this the data commands are there so .....
    elif "open power bi" in command or "power bi" in command:
        open_powerbi()
        return True

    elif "open excel" in command or "excel" in command:
        open_excel()
        return True

    elif "open jupyter notebook" in command or "jupyter notebook" in command:
        open_jupyter_notebook()
        return True

    elif "open anaconda" in command or "anaconda navigator" in command:
        open_anaconda()
        return True

    elif "open vscode" in command or "visual studio code" in command or "vs code" in command:
        open_vscode()
        return True

    elif "open mysql workbench" in command or "mysql workbench" in command:
        open_mysql_workbench()
        return True

    elif "open kaggle" in command or "kaggle" in command:
        open_kaggle()
        return True

    elif "open google colab" in command or "google colab" in command:
        open_google_colab()
        return True

    elif "open github" in command or "github" in command:
        open_github()
        return True

    elif "open pandas documentation" in command or "pandas documentation" in command:
        open_pandas_docs()
        return True

    elif "open numpy documentation" in command or "numpy documentation" in command:
        open_numpy_docs()
        return True

    elif "open matplotlib documentation" in command or "matplotlib documentation" in command:
        open_matplotlib_docs()
        return True

    elif "open seaborn documentation" in command or "seaborn documentation" in command:
        open_seaborn_docs()
        return True

    elif "open scikit learn documentation" in command or "scikit learn" in command:
        open_scikit_docs()
        return True


    elif (
            "stop" in command
            or "exit" in command
            or "goodbye" in command
            or "shutdown talkii" in command
    ):
        speak("Goodbye. Have a wonderful day.")
        return False

        # Any command that doesn't match the specific conditions above goes to Gemini
    else:
        reply = ask_ai(command)
        speak(reply)
        return True
