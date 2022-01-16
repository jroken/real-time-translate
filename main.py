#coded by Jroken
import pyttsx3
from googletrans import Translator
import speech_recognition as sr
from time import sleep
translator = Translator(service_urls=['translate.googleapis.com'])
bool = True
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 120)

def speak(x):
    engine.say(x)
    engine.runAndWait()
while bool:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening:" + str(r.energy_threshold))
        ses = r.listen(source, timeout=10, phrase_time_limit=10)
        print(r.recognize_google(ses, language='tr-tr'))
        kelime = r.recognize_google(ses, language='tr-tr')
        translator = Translator()
        example = translator.translate(kelime)
        print(example.text)
        speak(example.text)
#Coded By Jroken 12.01.2022
