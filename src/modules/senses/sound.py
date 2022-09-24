import speech_recognition as sr 
import pyttsx3
import pyaudio
from simhash import Simhash

listener = sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

print(Simhash('hello').value)
print(Simhash('hello1').value)

def talk(text:str):
    engine.say(text)
    engine.runAndWait()

def listen_on_microphone():
    try:
        with sr.Microphone(device_index=1) as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source=source)
            print('Now checking on google')
            command = listener.recognize_google(voice)
            print(command)
            if 'argon' in command:
                talk(command)
    except Exception as e:
        print(str(e))

listen_on_microphone()