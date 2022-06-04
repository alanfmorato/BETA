import speech_recognition as sr
import pyttsx3
import calculadora
import gravador
import pesquisa
import pomodoro
from tkinter import *
from tkcalendar import *
import datetime as dt
import reprodutor
import scraps
import clima

def principal():
    while True:
        audio = sr.Recognizer()
        maquina = pyttsx3.init()
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            inicializar = audio.recognize_google(voz, language='pt-BR')
            inicializar = inicializar.lower()
            try:
                if inicializar == 'olá':
                    maquina.say("Olá, sou a Bêta. Estou aqui para auxiliar. Gostaria de saber as funções que possuo?")
                    maquina.runAndWait()
                    print('Ouvindo...')
                    voz = audio.listen(source)
                    inicializar = audio.recognize_google(voz, language='pt-BR')
                    inicializar = inicializar.lower()
                    if inicializar == 'sim':
                        maquina.say("Possuo as seguintes funções: Calculadora, Scraps, Modo pomodoro, Pesquisa, Reprodução de música, "
                                "Gravador de voz e Clima")
                        maquina.runAndWait()
                    else:
                        maquina.say("Tudo bem! Vamos começar! O que deseja?")
                        maquina.runAndWait()
                else:
                    maquina.say("O que deseja hoje?")
                    maquina.runAndWait()
            except:
                maquina.say('Não te ouvi. O que deseja?')
                return inicializar
            try:
                with sr.Microphone() as ouvindo:
                    print('Ouvindo...')
                    voz = audio.listen(ouvindo)
                    chamado = audio.recognize_google(voz, language='pt-BR')
                    chamado = chamado.lower()
                    if 'calculadora' in chamado:
                        calculadora.calculadora()
                    elif 'pomodoro' in chamado:
                        pomodoro.pomodoro()
                    elif 'pesquisa' in chamado:
                        pesquisa.pesquisa()
                    elif 'calendário' in chamado:
                        root = Tk()
                        root.title("Calendário")
                        root.geometry("500x350")
                        root.config(bg="gray")
                        t_now = dt.datetime.now()  # Coleta data e hora atual
                        data = t_now.date()  # Coleta somente data atual
                        ano = int(data.strftime("%Y"))  # Coleta ano atual
                        mes = int(data.strftime("%m"))  # Coleta mes atual
                        dia = int(data.strftime("%d"))  # Coleta dia atual
                        cal = Calendar(root, select="day", year=ano, month=mes, day=dia)
                        cal.pack(pady=20, fill="both", expand="yes")
                        root.mainloop()
                    elif 'gravador de voz' in chamado:
                        gravador.gravador()
                    elif 'reproduzir vídeo' in chamado:
                        reprodutor.reprodutor()
                    elif 'livros' in chamado:
                        scraps.livros()
                    elif 'lembrete' in chamado:
                        print('lembrete')
                    elif 'clima' in chamado:
                        clima.clima()
                    else:
                        maquina.say('Obrigada por interagir comigo, até mais!')
                        maquina.runAndWait()
            except:
                maquina.say('Não te ouvi. O que deseja?')
                return chamado
            return principal()

