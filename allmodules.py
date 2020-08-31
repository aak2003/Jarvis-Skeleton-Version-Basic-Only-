import speech_recognition as sr
import time
import pyttsx3
import os
import wolframalpha as wf
from datetime import datetime
import pygame
import json
import nltk
import smtplib
import requests
from getaudio import getaudio
from getaudio import getsound
from email.message import EmailMessage

engine = pyttsx3.init()
engine.setProperty('volume',2.0)
engine.setProperty('rate', 150)

mic = sr.Microphone()
r = sr.Recognizer()

pygame.mixer.init()
pygame.init()