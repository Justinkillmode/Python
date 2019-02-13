import speech_recognition as sr
import sys
from gtts import gTTS
import os

# obtain audio from the microphone
while(True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
     #   print("Say something!")
        audio = r.listen(source)

# recognize speech using Sphinx

    try:
        if(r.recognize_google(audio, language="en_EN") == "Anna"):
            tts = gTTS(text="Wie kann ich dir helfen", lang='de')
            tts.save("wiekannichdirhelfen.mp3")
            os.system("wiekannichdirhelfen.mp3")
            
    except sr.RequestError as e:
        print("Anna error; {0}".format(e))
        