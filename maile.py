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
from selenium import webdriver
from email.message import EmailMessage
from getaudio import getaudio

EMAIL_ADDRESS = 'Your Email'
EMAIL_PASSWORD = 'Your Password'

engine = pyttsx3.init()
engine.setProperty('volume',2.0)
engine.setProperty('rate', 190)

def mail():
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    engine.say("who would you like to send it to")
    engine.runAndWait()
    rec = input("Sender email")
    #if "Aakash" in rec or "Akash" in rec or "myself" in rec:
        #msg['To'] = 'me@gmail.com' use this for contacts
    msg['To'] = rec
    engine.say("What is the subject sir")
    engine.runAndWait()
    msg['Subject'] = getaudio()
    engine.say("What would you like the content to be sir")
    engine.runAndWait()
    content = getaudio()
    msg.set_content(content)       
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        #server = smtplib.SMTP('localhost', 1025)
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        engine.say("Sir the email has been sent successfully")
        engine.runAndWait()
    except:
            engine.say('Sir,Something went wrong')
            engine.runAndWait()
mail()
if __name__ == 'main':
    getaudio()
