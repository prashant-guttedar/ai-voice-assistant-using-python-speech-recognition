import time
import webbrowser
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia
import random
import subprocess
import os
import platform

# ---------------- Text-to-Speech Setup ----------------
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Female voice (Microsoft Zira)
voices = engine.getProperty('voices')
for voice in voices:
    if "zira" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- Speech Recognition -----------------
def listen(timeout=5, phrase_time_limit=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            print("Listening...")
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            return ""
        except sr.RequestError:
            speak("Network error. Please check your connection.")
            return ""

# ---------------- Command Functions -----------------
def tell_time():
    current_time = time.strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def tell_date():
    today = datetime.today()
    date_str = today.strftime("%A, %B %d, %Y")
    speak(f"Today is {date_str}")

def open_website(site_name):
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "wikipedia": "https://www.wikipedia.org",
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
        "github": "https://www.github.com"
    }
    for name, url in websites.items():
        if name in site_name:
            webbrowser.open(url)
            speak(f"Opening {name}")
            return True
    return False

def play_youtube(song_name):
    url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
    webbrowser.open(url)
    speak(f"Playing {song_name} on YouTube")

def open_app(command):
    apps = {
        "cmd": "start cmd",
        "notepad": "notepad",
        "vs code": r"C:\Users\Niteen\AppData\Local\Programs\Microsoft VS Code\Code.exe",  # Change path
        "calculator": "calc",
    }
    for app_name, app_path in apps.items():
        if app_name in command:
            try:
                if app_name == "cmd":
                    os.system(app_path)
                else:
                    subprocess.Popen(app_path)
                speak(f"Opening {app_name}")
            except:
                speak(f"Failed to open {app_name}")
            return True
    return False

def lock_screen():
    os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.run("rundll32.exe user32.dll,LockWorkStation")
        elif os_name == "Linux":
            subprocess.run("gnome-screensaver-command -l", shell=True)
        elif os_name == "Darwin":
            subprocess.run("/System/Library/CoreServices/Menu\\ Extras/User.menu/Contents/Resources/CGSession -suspend", shell=True)
        speak("Screen locked")
    except:
        speak("Failed to lock screen")

def respond_to_greeting(command):
    greetings = ["hello", "hi", "hey"]
    for greet in greetings:
        if greet in command:
            speak("Hello! How can I help you?")
            return True
    if "how are you" in command:
        speak("I am good, thank you! What about you?")
        return True
    return False

def tell_joke():
    jokes = [
        "Why did the computer show up at work late? It had a hard drive!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the Python developer go broke? Because he used up all his cache!"
    ]
    speak(random.choice(jokes))

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except:
        speak("I could not find anything on Wikipedia for that.")

def calculate(expression):
    try:
        result = eval(expression)
        speak(f"The answer is {result}")
    except:
        speak("Sorry, I cannot calculate that.")

def weather():
    speak("Which city do you want the weather for?")
    city = listen()
    if not city:
        speak("I did not hear the city name.")
        return
    url = f"https://www.google.com/search?q=weather+{city.replace(' ', '+')}"
    webbrowser.open(url)
    speak(f"Here is the weather for {city} on Google")

# ---------------- Main Assistant Loop -----------------
def main():
    speak("Hello! I am your assistant. I can tell time, date, jokes, search Wikipedia, play YouTube, open websites and apps, show weather, calculate, and lock the screen.")
    
    while True:
        command = listen()
        if command:
            if "stop" in command or "exit" in command:
                speak("Goodbye! Have a nice day.")
                break
            elif respond_to_greeting(command):
                continue
            elif "time" in command:
                tell_time()
            elif "date" in command or "day" in command:
                tell_date()
            elif "play" in command:
                play_youtube(command.replace("play", "").strip())
            elif "open" in command:
                if not open_website(command) and not open_app(command):
                    speak("Sorry, I don't know that website or app.")
            elif any(phrase in command for phrase in ["lock screen", "screen lock", "lock my computer"]):
                lock_screen()
            elif "weather" in command:
                weather()
            elif "who is" in command or "what is" in command or "tell me about" in command:
                search_wikipedia(command)
            elif "joke" in command:
                tell_joke()
            elif any(char.isdigit() for char in command) and any(op in command for op in "+-*/"):
                calculate(command)
            else:
                speak("Sorry, I don't understand. You can ask me about time, date, play YouTube, open apps or websites, weather, Wikipedia, jokes, calculations, or lock screen.")
        else:
            print("I didn't hear anything, please try again.")

if __name__ == "__main__":
    main()
