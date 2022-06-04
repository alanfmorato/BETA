import speech_recognition as sr
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
import os

def gravador():
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.runAndWait()
    with sr.Microphone() as source:
            maquina.say('Vamos começar, se prepare!')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            freq = 44100
            seconds = 5
            gravacao = sd.rec(int(seconds * freq), samplerate=freq, channels=2)
            maquina.say("Começando: Fale agora!!")
            sd.wait()
            maquina.say("Fim da gravação!")
            write('output.wav', freq, gravacao)
            os.startfile("output.wav")