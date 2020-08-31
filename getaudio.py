import speech_recognition as sr
import time
import pyttsx3
import os
import wolframalpha as wf
from datetime import datetime
import pygame
import json
import smtplib
import requests
from email.message import EmailMessage

def getaudio():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")
        # recording the audio using speech recognition
        audio = rObject.listen(source)
        print("Stop.")  # limit 5 secs

        while True:
            try:
                text = rObject.recognize_google(audio, language='en-US')
                print("You : ", text)
                return text
            except:
                print("Issue Understanding audio")
                return getaudio()

def getsound():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("waiting for wakeword")
        # recording the audio using speech recognition
        audio = rObject.listen(source)
        print("Stop.")  # limit 5 secs

        while True:
            try:
                text = rObject.recognize_google(audio, language='en-US')
                print("You : ", text)
                return text
            except:
                print("Issue Understanding audio")
                return getsound()

def getaveragewordsminute():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Please speak for 10 seconds so we can calculate the amount of words you can speak in a minute at an average")
        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=10)
        print("Stop.")  # limit 10 secs

        while True:
            try:
                text = rObject.recognize_google(audio, language='en-US')
                print("You said : ", text , "\n We have successfully calculated your average")
                return text
            except:
                print("Issue Understanding audio")
                return getaveragewordsminute()