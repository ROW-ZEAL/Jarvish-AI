import datetime
import speech_recognition as sr
import os
import webbrowser
import subprocess
import random

def say(text):
    os.system(f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source) 
        try:
            print("recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Sorry, I couldn't understand."

def get_time_of_day():
    current_time = datetime.datetime.now()
    if 5 <= current_time.hour < 12:
        return "morning"
    elif 12 <= current_time.hour < 17:
        return "afternoon"
    elif 17 <= current_time.hour < 21:
        return "evening"
    else:
        return "night"

def open_application(app_name):
    if "notepad" in app_name:
        subprocess.Popen(["notepad.exe"])
        return "Notepad is opened, sir."
    elif "calculator" in app_name:
        subprocess.Popen(["calc.exe"])
        return "Calculator is opened, sir."
    # Add more applications as needed


if __name__ == '__main__':
    print("Initializing Jarvis...")
    time_of_day = get_time_of_day()
    if time_of_day == "morning":
        say("Good morning, I am Jarvis A.I.")
    elif time_of_day == "afternoon":
        say("Good afternoon, I am Jarvis A.I.")
    elif time_of_day == "evening":
        say("Good evening, I am Jarvis A.I.")
    else:
        say("Good night, I am Jarvis A.I.")

    while True:
        print("Listening...")
        query = take_command()

        if "open" in query:
            app_name = query.split("open", 1)[1].strip()
            response = open_application(app_name)
            say(response)


        sites = [
            ["Google", "https://www.google.com"],
            ["Wikipedia", "https://www.wikipedia.org"],
            ["ChatGPT", "https://www.openai.com/chatgpt"],
            ["YouTube", "https://www.youtube.com"]
        ]

        for site in sites:   
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Boss .....")
                webbrowser.open(site[1])

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%I")
            minute = datetime.datetime.now().strftime("%M")
            time_period = datetime.datetime.now().strftime("%p").lower()
            say(f"Sir, the time is {hour} {minute} {time_period}")

        elif "the date" in query:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            say(f"Sir, today's date is {date}")

        elif "Jarvis exit".lower() in query.lower():
            say("Jarvis is out of battery. It is shutting down!")
            exit()
