import speech_recognition
import pyttsx3
import webbrowser
import os
import time
import requests
import json
from datetime import date

#nghe
ca_ear = speech_recognition.Recognizer()   # khoi tao chuc nang nghe
ca_mouth = pyttsx3.init()
ca_brain = ""

# --------------function------------------------------------------

# bitcoin
def bitcoin():
    url = requests.get("https://blockchain.info/ticker")
    get = url.json()
    usd = get["USD"]

    sell = str(usd["sell"])


while True:
    with speech_recognition.Microphone() as mic:  # tao mic de nghe am thanh
        print("Ca: I'm Listening...")
        time.sleep(0.8)
        audio = ca_ear.listen(mic)  # dung mic nghe de tao nen 1 file am thanh

    print("Ca: *nao load cac thu*")
    try:
        you = ca_ear.recognize_google(audio)   # nhan dien giong noi tu file am thanh
    except:
        you = ""
        # neu nhu khong nhan dien duoc giong noi no se tra lai kq nhu tren
    print("You: " + you)

    # hieu
    if you == "":
        ca_brain = "I do not know what you're saying \nTry again :>"
    elif "hello" in you:
        ca_brain = "hello Khoa handsome"
    elif "your name" in you:
        ca_brain = "my name is Ca"
    elif "how are you" in you:
        ca_brain = "I'm fine thank you and you"
    elif "fine" in you:
        ca_brain = "yeah, it so good"
    elif "coin" in you:
        ca_brain = "1 bitcoin costs: " + bitcoin()
    elif "today" in you:
        today = date.today()
        ca_brain = "today: " + today.strftime("%B %d, %Y")
    elif "music" in you:
        ca_brain = "what is the name of the song you are looking for?"
    elif "list" in you:
        webbrowser.open('https://www.youtube.com/watch?v=95rgl0IFa7k&list=PL8Qn8mHBuDbhtdTchwrj3IxXlU7GO6sgp&index=2&t=0s')
        ca_brain = "Open your list music"
    elif "Spotify" in you:
        ca_brain = "open spotify"
        os.system("start Spotify:")
    elif "Google" in you:
        ca_brain = "open Google"
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    elif "YouTube" in you:
        ca_brain = "Open Youtube"
        webbrowser.open('https://www.youtube.com')
    elif "Facebook" in you:
        ca_brain = "open facebook"
        webbrowser.open('https://www.facebook.com')
    elif "Messenger" in you:
        ca_brain = "open messenger"
        webbrowser.open("https://www.messenger.com")
    elif "chill" in you:
        ca_brain = "open chill music"
        webbrowser.open("https://www.youtube.com/playlist?list=PL8Qn8mHBuDbj1EfwkRytwBg_UkhV_f9Id")
    elif "Gmail" in you:
        ca_brain = "open gmail"
        webbrowser.open("https://mail.google.com/mail/u/0/")
    elif "sb3" in you:
        ca_brain = "open sublime text 3"
        os.startfile('D:\Sublime Text 3\sublime_text.exe') 
    elif "Steam" in you:
        ca_brain = "open steam"
        os.startfile("D:\Steam\Steam.exe")
    elif "bye" in you:
        ca_brain = "bye bye"
        ca_mouth.say(ca_brain)
        ca_mouth.runAndWait()
        break
    else:
        ca_brain = "Sorry I have not been programmed for this saying :<"

    print(ca_brain)
    ca_mouth.say(ca_brain)
    ca_mouth.runAndWait()