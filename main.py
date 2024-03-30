# libraries i use
# import pyttsx3
import webbrowser
import random
from random import randint
import datetime
import wikipedia
import sentences
import requests, json
import speech_recognition as sr
from googlesearch import search
import os
from function import *

# from colorama import init
# from termcolor import colored
# init()


r = sr.Recognizer()

speak("what is your name?")
name = str(input("what is your name >>> "))


# function for telling the user
def greeting():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("good morning " + name + ", how are you")
        speak("good morning " + name + ", how are you")

    elif 12 <= hour < 18:
        print("good afternoon " + name + ", how are you")
        speak("good afternoon " + name + ", how are you")

    else:
        print("good evening " + name + ", how are you")
        speak("good evening " + name + ", how are you")


greeting()

####
####
####

while True:

    try:
        with sr.Microphone() as source:
            print("Speak anything >>> ")
            audio = r.listen(source)

            text = r.recognize_google(audio)
            print(">>>>{}".format(text))

            # i am fine ...
            for good in sentences.fine:
                try:
                    if good in text:
                        g = random.choice(sentences.great)
                        print(g)
                        speak(g)
                except Exception as e:
                    print(e)

            # asking the name
            try:
                if "your name" in text:
                    print("my name is Bruno")
                    speak("my name is Bruno")
            except Exception as e:
                print(e)

            # wikipedia
            for wikiup in sentences.wiki:
                try:
                    if wikiup in text and "what is your name" != text and "what can you do" != text and "what's your name" != text and "what are you doing" != text:
                        p = wikipedia.summary(text, sentences=5)
                        print(p)
                        speak(p)
                        webbrowser.open(text)
                        for j in search(text, tld="co.in", num=1, stop=5, pause=2):
                            print(j)
                except Exception as e:
                    print(e)

            # date and time
            try:
                if "date" in text or "time" in text:
                    y = datetime.datetime.now()
                    print(y.strftime("%c"))
                    speak(y.strftime("%c"))
            except Exception as e:
                print(e)

            # what can you do
            try:
                if "what can you do" in text:
                    for work in sentences.job:
                        print(work)
                        speak(work)
            except Exception as e:
                print(e)

            # how are you
            for wearying in sentences.how:
                try:
                    if wearying in text:
                        s = random.choice(sentences.fine)
                        print(s)
                        speak(s)
                except Exception as e:
                    print(e)

            # weather
            try:
                if "weather" in text:
                    URL = "http://api.openweathermap.org/data/2.5/weather?q=beirut&appid=a45c96282a65075ec7646112272394b9"
                    response = requests.get(URL)
                    if response.status_code == 200:
                        data = response.json()
                        main = data["main"]
                        temperature = main["temp"]
                        humidity = main["humidity"]
                        pressure = main["pressure"]

                        print(f"Temperature: {int(temperature - 273.15)} Celsius")
                        speak(f"Temperature: {int(temperature - 273.15)} Celsius")
                        print(f"Humidity: {humidity}")
                        speak(f"Humidity: {humidity}")
                        print(f"Pressure: {pressure}")
                        speak(f"Pressure: {pressure}")

                    else:
                        print("Error in the HTTP request")
                        speak("Error in the HTTP request")
            except Exception as e:
                print(e)

            # what are you doing
            for do in sentences.work:
                try:
                    if do in text:
                        a = random.choice(sentences.doing)
                        print(a)
                        speak(a)
                except Exception as e:
                    print(e)

            # thank you
            for merci in sentences.thanks:
                try:
                    if merci in text:
                        n = random.choice(sentences.welcome)
                        print(n)
                        speak(n)
                except Exception as e:
                    print(e)

            # tell something
            for joke in sentences.some:
                try:
                    if joke in text:
                        m = random.choice(sentences.something)
                        print(m)
                        speak(m)
                except Exception as e:
                    print(e)

            # i am sad
            for bad in sentences.sad:
                try:
                    if bad in text:
                        b = random.choice(sentences.happiness)
                        print(b)
                        speak(b)
                except Exception as e:
                    print(e)

            # i love you
            for attract in sentences.friend:
                try:
                    if attract in text:
                        c = random.choice(sentences.love)
                        print(c)
                        speak(c)
                except Exception as e:
                    print(e)

            # i want to play
            try:
                if "play" in text:
                    e = random.choice(sentences.play)
                    print(e)
                    speak(e)
                    d = int(input("enter choices 1/2 : "))

                    if d == 1:
                        print("we will play the guessing number")
                        speak("we will play the guessing number")
                        for i in range(5):
                            guessinggame()

                    elif d == 2:
                        print("we will play rock paper scissors")
                        speak("we will play rock paper scissors")
                        for i in range(5):
                            rockpaperscissors()
            except Exception as e:
                print(e)

            # calculator
            try:
                if "calculator" in text:
                    f = random.choice(sentences.play)
                    print(f)
                    speak(f)
                    for i in range(1, 6):
                        calculator()
            except Exception as e:
                print(e)

            # BYE
            for cheerio in sentences.bye:
                try:
                    if cheerio in text:
                        z = random.choice(sentences.bye)
                        print(z)
                        speak(z)
                        speak("do you want to shutdown you laptop sir , [yes or no] ? ")
                        k = input(" Do you want to shutdown your laptop sir , [y/n] ? ")
                        if k == "y" or k == "yes":
                            os.system("shutdown /s /t 30")
                            exit()
                        else:
                            exit()
                except Exception as e:
                    print(e)

    except Exception as e:
        pass

else:
    pass