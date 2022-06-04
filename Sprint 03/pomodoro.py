import speech_recognition as sr
import pyttsx3
import time
from tkinter import messagebox
import winsound
import datetime as dt
def pomodoro():
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.runAndWait()
    with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            t_now = dt.datetime.now()  
            t_pom = 25 * 60 
            t_delta = dt.timedelta(0, t_pom)  
            t_fut = t_now + t_delta  
            delta_sec = 5 * 60  
            t_fin = t_now + dt.timedelta(0, t_pom + delta_sec) 

            pomodoro = pyttsx3.init()
            pomodoro.say("Pomodóro iniciado " "\n\nAgora é " + t_now.strftime(
                "%H:%M") + " hrs. \n\nTemporizador definido por 25 minutos")
            pomodoro.runAndWait()

            total_pomodoros = 0
            breaks = 0

            
            while True:
                if dt.datetime.now() < t_fut:
                    print('Pomodóro')
                elif t_fut <= dt.datetime.now():
                    if total_pomodoros in range(3, 100, 5):
                        for i in range(1):
                            winsound.Beep((i + 400), 500) 

                        print('Hora do intervalo! Você tem 25 minutos de descanso.')
                        breaks += 1
                        audio = sr.Recognizer()
                        pomodoro = pyttsx3.init()
                        pomodoro.say('Hora do intervalo!')
                        pomodoro.runAndWait()
                        time.sleep(
                            5)  
                        print("Foi")
                    if breaks == 0:
                        for i in range(2):
                            winsound.Beep((i + 400), 700) 
                        print('Hora do intervalo!')
                        breaks += 1
                        audio = sr.Recognizer()
                        pomodoro = pyttsx3.init()
                        pomodoro.say('Hora do intervalo! Você tem 5 minutos de descanso.')
                        pomodoro.runAndWait()
                        time.sleep(
                            5) 
                    else:
                        print('Fim')
                        breaks = 0

                        for i in range(1):
                            winsound.Beep((i + 400), 700) 
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
