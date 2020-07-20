import speech_recognition

ca_ear = speech_recognition.Recognizer()   # khoi tao chuc nang nghe
with speech_recognition.Microphone() as mic:  # tao mic de nghe am thanh
    print("Ca: I'm Listening...")
    audio = ca_ear.listen(mic)  # dung mic nghe de tao nen 1 file am thanh
try:
    you = ca_ear.recognize_google(audio)   # nhan dien giong noi tu file am thanh
except:
    you = "I do not know what you're saying -_- \nTry again :>"
    # neu nhu khong nhan dien duoc giong noi no se tra lai kq nhu tren
print(you)  # doc giong noi da nhan dien