Python Voice Assistant Done By Prashant Guttedar 
YOUTUBE CHANNEL @pythonaimlprojects 

Overview

This Python-based Voice Assistant listens to user commands, processes speech, and performs tasks such as:

Greeting the user

Telling time and date

Opening websites and applications

Fetching weather information

Searching Wikipedia

Playing YouTube videos

Performing calculations

Controlling smart devices

Responding via GPT/OpenAI

It is designed to have both beginner-level and advanced functionality.


Beginner-Level Features

HOW TO RUN?
python Beginner.py

Responds to greetings like "Hello" or "Hi"

Tells the current time and date

Performs Google searches

Opens websites such as Google, YouTube, Wikipedia, GitHub

Opens local applications like Notepad, CMD

Plays YouTube videos in browser

Converts speech to text



Advanced Features  
HOW TO RUN ?
python Advanced.py

Fetches live weather information using Google search

Summarizes topics using the Wikipedia API

Plays YouTube videos in a Selenium-controlled browser

Controls smart devices (lights, fan, AC)

Responds to GPT/OpenAI queries

Locks the computer screen

Performs calculations from voice commands

Opens advanced applications like Visual Studio Code

Integrates text-to-speech for dynamic voice responses

Technology Stack

Python 3.10+

SpeechRecognition – Speech-to-text

PyAudio – Capturing microphone input

pyttsx3 – Text-to-speech engine

wikipedia – Wikipedia API

requests – HTTP requests

selenium – Browser automation

chromedriver-autoinstaller – Automatic ChromeDriver setup

pyautogui – GUI automation

pywhatkit – YouTube/WhatsApp automation

openai – GPT queries

Installation

Clone the repository:

git clone https://github.com/YourUsername/voice-assistant.git
cd voice-assistant


Install dependencies:

# Beginner features
pip install SpeechRecognition PyAudio pyttsx3 wikipedia requests

# Advanced features
pip install selenium chromedriver-autoinstaller pyautogui pywhatkit openai


(Optional) For Selenium YouTube automation, ensure Google Chrome is installed. chromedriver_autoinstaller will handle the ChromeDriver automatically.

Replace the OpenAI API key in your code:

openai.api_key = "YOUR_OPENAI_API_KEY"

Usage

Run the assistant:

python main.py


Say "Hey Assistant" to start listening.

Commands you can give:

Greetings: "Hello"

Time/Date: "What is the time?", "What is today's date?"

YouTube: "Play Kesariya song"

Websites: "Open YouTube", "Open Google"

Applications: "Open Notepad", "Open CMD", "Open VS Code"

Weather: "What is the weather in London?"

Wikipedia/Knowledge: "Who is Albert Einstein?", "Tell me about Python"

Smart devices: "Turn on the light", "Turn off the fan"

Calculations: "5 plus 3", "10 divided by 2"

Jokes: "Tell me a joke"

Lock computer: "Lock my computer"

To stop the assistant, say: "Stop" or "Exit".

Notes

Works best with a good microphone and stable internet connection.

For Windows, if PyAudio fails to install, download the appropriate .whl file from PyAudio binaries
 and install using pip install filename.whl.

Ensure paths to applications (e.g., VS Code) are correctly set in the code.

Selenium YouTube automation requires Google Chrome installed.

License

This project is open-source and free to use under the MIT License