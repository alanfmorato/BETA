
import speech_recognition as sr
import wikipedia
import pyttsx3
import time
from tkinter import messagebox
import winsound
from tkinter import *
from tkcalendar import *
import datetime as dt
import pywhatkit
import sounddevice as sd
from scipy.io.wavfile import write
import os

while True:
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.say('Olá, meu nome é beta. Qual função deseja acessar: Pesquisa, Pomodóro, Datas, Reprodutor ou Gravador de voz')
    maquina.runAndWait()


    def executa_comando():

        try:
            with sr.Microphone() as source:
                print('Ouvindo...')
                voz = audio.listen(source)
                comando = audio.recognize_google(voz, language='pt-BR')
                comando = comando.lower()

                if 'beta' in comando:
                    comando = comando.replace('beta', '')
                    maquina.say(comando)
                    maquina.runAndWait()
        except:
            print('Microfone não está conectado')
        return comando


    def comando_voz_usuario():
        comando = executa_comando()
        if 'pesquisa' in comando:
            procurar = comando.replace('pesquisa', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, 2)
            maquina.say(resultado)
            maquina.runAndWait()
        elif 'datas' in comando:
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
        elif 'pomodoro' in comando:

            t_now = dt.datetime.now()  # data e hora atual;

            t_pom = 25 * 60  # tempo de duração do fluxo pomodoro 25m;

            t_delta = dt.timedelta(0, t_pom)  # diferença de tempo;

            t_fut = t_now + t_delta  # hora que o pomodoro termina e começa a pausa;

            delta_sec = 5 * 60  # definição de intervalo;

            t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)  # hora que a pausa termina;

            pomodoro = pyttsx3.init()

            pomodoro.say("Pomodóro iniciado " "\n\nAgora é " + t_now.strftime(

                "%H:%M") + " hrs. \n\nTemporizador definido por 25 minutos")

            pomodoro.runAndWait()

            total_pomodoros = 0

            breaks = 0

            # Looping simples dividido em três seções: Hora pomodoro, intervalo e fim do código;

            while True:

                if dt.datetime.now() < t_fut:

                    print('Pomodóro')

                elif t_fut <= dt.datetime.now():

                    if total_pomodoros in range(3, 100, 5):

                        for i in range(1):
                            winsound.Beep((i + 400), 500)  # Primeiro número é referente ao volume do bip.

                        print('Hora do intervalo! Você tem 25 minutos de descanso.')

                        breaks += 1

                        audio = sr.Recognizer()

                        pomodoro = pyttsx3.init()

                        pomodoro.say('Hora do intervalo!')

                        pomodoro.runAndWait()

                        time.sleep(
                            5)  # Por conta do delay da fala subtrair do tempo de pausa um tempo,então o que era pra ser 25 min ficou 21 min

                        print("Foi")

                    if breaks == 0:

                        for i in range(2):
                            winsound.Beep((i + 400), 700)  # Primeiro número é referente ao volume do bip.

                        print('Hora do intervalo!')

                        breaks += 1

                        audio = sr.Recognizer()

                        pomodoro = pyttsx3.init()

                        pomodoro.say('Hora do intervalo! Você tem 5 minutos de descanso.')

                        pomodoro.runAndWait()

                        time.sleep(
                            5)  # Por conta do delay da fala subtrair do tempo de pausa um tempo,então o que era pra ser 5 min ficou o tempo determinado como 1260 dividido por 5, pra ficar um descanso proporcional.

                    else:

                        print('Fim')

                        breaks = 0

                        for i in range(1):
                            winsound.Beep((i + 400), 700)  # Primeiro número é referente ao volume do bip.

                            audio = sr.Recognizer()

                            pomodoro = pyttsx3.init()

                            pomodoro.say('O intervalo acabou, deseja iniciar um novo pomodóro?')

                            pomodoro.runAndWait()

                        usr_ans = messagebox.askyesno("Fim da primeira sequência do pomodóro",

                                                      "Deseja iniciar outra sequência de pomodóro?")

                        total_pomodoros += 1

                        print(total_pomodoros)

                        if usr_ans == True:

                            t_now = dt.datetime.now()

                            t_fut = t_now + dt.timedelta(0, t_pom)

                            t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)


                        elif usr_ans == False:

                            msg = messagebox.showinfo("Fim do pomodóro",

                                                      "\nVocê completou " + str(total_pomodoros) + " pomodóro(s) hoje!")

                            break

                    print("sleeping")

                    time.sleep(1)

                    t_now = dt.datetime.now()

                    timenow = t_now.strftime("%H:%M")
        elif 'gravador de voz' in comando:
            freq = 44100
            seconds = 10
            
            gravacao = sd.rec(int(seconds * freq), samplerate=freq, channels=2)
            print("Começando: Fale agora!!")
            sd.wait()
            print("Fim da gravação!")
            write('output.wav', freq, gravacao)
            os.startfile("output.wav")

    comando_voz_usuario()
