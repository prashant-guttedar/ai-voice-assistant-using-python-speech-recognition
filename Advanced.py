import time
import subprocess
import wikipedia
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import openai

# ------------------- Configuration -------------------
openai.api_key = "YOUR_OPENAI_API_KEY"

# ------------------- Text-to-Speech -------------------
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ------------------- Listen Function -------------------
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

# ------------------- YouTube Controller -------------------
class YouTubePlayer:
    def __init__(self):
        chromedriver_autoinstaller.install()
        self.driver = None

    def open_youtube(self):
        if self.driver is None:
            options = Options()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=options)
            self.driver.get("https://www.youtube.com")
            time.sleep(2)

    def play_song(self, song_name):
        self.open_youtube()
        try:
            search_box = self.driver.find_element(By.NAME, "search_query")
            search_box.clear()
            search_box.send_keys(song_name)
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)
            videos = self.driver.find_elements(By.ID, "video-title")
            if videos:
                videos[0].click()
                speak(f"Playing {song_name} on YouTube")
            else:
                speak("Sorry, I could not find that song.")
        except Exception as e:
            print(e)
            speak("Error accessing YouTube.")

# ------------------- Local Apps -------------------
def open_app(command):
    apps = {
        "cmd": "cmd",
        "notepad": "notepad",
    }
    for app_name, app_path in apps.items():
        if app_name in command:
            try:
                subprocess.Popen(app_path)
                speak(f"Opening {app_name}")
            except Exception as e:
                speak(f"Failed to open {app_name}")
            return True
    return False

# ------------------- GPT / Wikipedia -------------------
def answer_general_knowledge(query):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query,
            max_tokens=150
        )
        answer = response['choices'][0]['text'].strip()
        speak(answer)
    except:
        try:
            summary = wikipedia.summary(query, sentences=2)
            speak(f"According to Wikipedia: {summary}")
        except:
            speak("Sorry, I could not find information on that topic.")

# ------------------- Main Loop -------------------
def main():
    yt = YouTubePlayer()
    speak("Hello! I am your assistant. You can give me commands directly.")

    while True:
        command = listen()
        if not command:
            continue

        if "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
        elif "play" in command:
            song_name = command.replace("play", "").strip()
            yt.play_song(song_name)
        elif open_app(command):
            pass
        else:
            answer_general_knowledge(command)

if __name__ == "__main__":
    main()
