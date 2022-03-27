
import speech_recognition as sr

# Criando um reconhecedor

r = sr.Recognizer

# abrir o microfone

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    print(r.recognize_google(audio, language = 'pt'))
