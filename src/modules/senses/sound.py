import speech_recognition as sr 
import pyttsx3
import pyaudio

listener = sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


def play(audio):
    '''
    Play audio captured from microphone
    '''
    CHUNK = 1024
    
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(audio.sample_width),
        channels=1,
        rate=audio.sample_rate,
        output=True
    )
    
    wav = audio.get_wav_data()
    
    stream.write(wav)
    stream.close()
    
    p.terminate()

def talk(text:str):
    engine.say(text)
    engine.runAndWait()

def listen_on_microphone():
    try:
        while True:
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