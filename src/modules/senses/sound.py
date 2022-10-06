import os
import pyttsx3
import pyaudio
from hashlib import md5
# from dejavu import Dejavu
from datetime import datetime
import speech_recognition as sr 
# from dejavu.recognize import FileRecognizer

listener = sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

audio_folder = 'audio'


# djv = Dejavu({
#     #'database_backend': 'orm',
#     #'database_uri': 'sqlite:///',
#     'database': {
#         'host': '127.0.0.1',
#         'user': 'root',
#         'password': '',
#         'db': 'dejavu'
#     }
# })

# def save_audio(audio, filename: str = None)->str:
#     '''
#     Save Captured audio from microphone
    
#     @param audio str
#     @return filename str
#     '''
#     filename = filename if filename else os.path.join(os.curdir, audio_folder, md5(audio.frame_data).hexdigest())+'.wav'
    
#     with open(filename, 'wb') as file:
#         file.write(audio.get_wav_data())
    
#     return filename

# def fingerprint_audio(filename: str):
#     '''
#     Fingerprint audio for recognition
    
#     @param audio File Name
#     '''
#     match = djv.recognize(FileRecognizer, filename)

#     if not match:
#         djv.fingerprint_file(filename)
#     else:
#         print(match)
        
# def play(audio):
#     '''folder = 'audio_files'
#     Play audio captured from microphone
#     '''
#     CHUNK = 1024
    
#     p = pyaudio.PyAudio()
#     stream = p.open(
#         format=p.get_format_from_width(audio.sample_width),
#         channels=1,
#         rate=audio.sample_rate,
#         output=True
#     )

#     stream.write(audio.get_wav_data())
#     stream.close()
    
#     p.terminate()

def talk(text:str):
    engine.say(text)
    engine.runAndWait()

def listen_on_microphone():
    # try:
    while True:
        with sr.Microphone(device_index=1) as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source=source)
            print('Now checking on google')
            # filename = save_audio(voice)
            # fingerprint_audio(filename)
            command = listener.recognize_google(voice)
            print(command)
            talk(command)
            # if 'argon' in command:
            #     talk(command)
    # except Exception as e:
    #     print(str(e))

if __name__ == '__main__':
    listen_on_microphone()
