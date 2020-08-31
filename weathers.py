import speech_recognition as sr
import time
import pyttsx3
import os
from datetime import datetime
import pygame
import json
import smtplib
import requests
import wikipediaapi
from selenium import webdriver
from getaudio import getaudio
from getaudio import getsound
from email.message import EmailMessage


engine = pyttsx3.init()
engine.setProperty('volume',2.0)
engine.setProperty('rate', 190)

def weather():
    api_key = "ae70e6d11967aac0f7687946b014848d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Your city name"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"] 
        current_temperature = (y["temp"]-273.15)//1
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
        engine.say("sir The current temperature is " + str(current_temperature) + "degrees celsius , humidity is" + str(current_humidiy) + " percent and description is" + str(weather_description))
        engine.runAndWait()
        from main import initialization
        initialization()
    else:
        engine.say("sir something went wrong while I was fetching weather data")
        engine.runAndWait()
        from main import initialization
        initialization()
weather()
