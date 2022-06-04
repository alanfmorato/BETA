import speech_recognition as sr
import wikipedia
import pyttsx3
def pesquisa():
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.runAndWait()
    with sr.Microphone() as source:
        print('ouvindo pesquisa')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        procurar = comando.replace('pesquisa', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        maquina.say(resultado)
        maquina.runAndWait()