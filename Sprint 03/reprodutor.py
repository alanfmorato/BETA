import speech_recognition as sr
import pyttsx3
import pywhatkit

def reprodutor():
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.runAndWait()
    with sr.Microphone() as source:
        print('Ouvindo...')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando')
        maquina.runAndWait()