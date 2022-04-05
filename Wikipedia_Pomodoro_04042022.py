import speech_recognition as sr
import wikipedia
import pyttsx3
import time
import datetime as dt
from tkinter import *
from tkinter import messagebox
import winsound


while True:
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.say('Olá, meu nome é Helpy, qual função deseja acessar, Pesquisa, Pomodóro')
    maquina.runAndWait()


    def executa_comando():

        try:
            with sr.Microphone() as source:
                print('Ouvindo...')
                voz = audio.listen(source)
                comando = audio.recognize_google(voz, language='pt-BR')
                comando = comando.lower()

                if 'Helpy' in comando:
                    comando = comando.replace('Helpy', '')
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

        elif 'pomodoro':
            def center(win):
                # :param win: the main window or Toplevel window to center

                # Apparently a common hack to get the window size. Temporarily hide the
                # window to avoid update_idletasks() drawing the window in the wrong
                # position.
                win.update_idletasks()  # Update "requested size" from geometry manager

                # define window dimensions width and height
                width = win.winfo_width()
                frm_width = win.winfo_rootx() - win.winfo_x()
                win_width = width + 2 * frm_width

                height = win.winfo_height()
                titlebar_height = win.winfo_rooty() - win.winfo_y()
                win_height = height + titlebar_height + frm_width

                # Get the window position from the top dynamically as well as position from left or right as follows
                x = win.winfo_screenwidth() // 2 - win_width // 2
                y = win.winfo_screenheight() // 2 - win_height // 2

                # this is the line that will center your window
                win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

                # This seems to draw the window frame immediately, so only call deiconify()
                # after setting correct window position
                win.deiconify()

            t_now = dt.datetime.now()  # data e hora atual;
            t_pom = 25 * 60  # tempo de duração do fluxo pomodoro 25m;
            t_delta = dt.timedelta(0, t_pom)  # diferença de tempo;
            t_fut = t_now + t_delta                                    # hora que o pomodoro termina e começa a pausa;
            delta_sec = 5 * 60                                                               # definição de intervalo;
            t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)  # hora que a pausa termina;

            janela = Tk()
            janela.title("Pomodoro")

            texto = Label(janela, text="Pomodoro iniciado " "\n\nAgora é " + t_now.strftime("%H:%M") + " hrs. \n\nTemporizador definido por 25 minutos")
            texto.grid(column=0, row=0, padx=10, pady=10)
            janela.attributes("-topmost", True)
            janela.iconbitmap('')  # Colocar o diretorio da imagem em '.ico'.
            center(janela)
            janela.mainloop()
            audio = sr.Recognizer()
            maquina = pyttsx3.init()
            maquina.say('O pomodóro de 25 minutos se iniciará!')
            maquina.runAndWait()

            total_pomodoros = 0
            breaks = 0

            # Looping simples dividido em três seções: Hora pomodoro, intervalo e fim do código;
            while True:
                if dt.datetime.now() < t_fut:
                    print('Pomodoro')
                elif t_fut <= dt.datetime.now():
                    if total_pomodoros in range(3, 100, 5):
                        for i in range(1):
                            winsound.Beep((i + 400), 500)  # Primeiro número é referente ao volume do bip.
                        print('Hora do intervalo! Você tem 25 minutos de descanso.')

                        breaks += 1

                        audio = sr.Recognizer()
                        maquina = pyttsx3.init()
                        maquina.say('Hora do intervalo!')
                        maquina.runAndWait()
                        time.sleep(1260)  # Por conta do delay da fala subtrair do tempo de pausa um tempo,então o que era pra ser 25 min ficou 21 min
                        print("Foi")
                    if breaks == 0:
                        for i in range(2):
                            winsound.Beep((i + 400), 700)  # Primeiro número é referente ao volume do bip.
                        print('Hora do intervalo!')

                        breaks += 1

                        audio = sr.Recognizer()
                        maquina = pyttsx3.init()
                        maquina.say('Hora do intervalo! Você tem 5 minutos de descanso.')
                        maquina.runAndWait()
                        time.sleep(252)  # Por conta do delay da fala subtrair do tempo de pausa um tempo,então o que era pra ser 5 min ficou o tempo determinado como 1260 dividido por 5, pra ficar um descanso proporcional.

                    else:
                        print('Fim')
                        breaks = 0

                        for i in range(1):
                            winsound.Beep((i + 400), 700)  # Primeiro número é referente ao volume do bip.
                            audio = sr.Recognizer()
                            maquina = pyttsx3.init()
                            maquina.say('O intervalo acabou, deseja iniciar um novo pomodóro?')
                            maquina.runAndWait()
                        usr_ans = messagebox.askyesno("Fim da primeira sequência do pomodoro",
                                                      "Deseja iniciar outra sequência de pomodoro?")
                        total_pomodoros += 1
                        print(total_pomodoros)

                        if usr_ans == True:

                            t_now = dt.datetime.now()
                            t_fut = t_now + dt.timedelta(0, t_pom)
                            t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)

                        elif usr_ans == False:
                            messagebox.showinfo("Fim do pomodoro",
                                                "\nVocê completou " + str(total_pomodoros) + " pomodoro(s) hoje!")
                            break

                    print("sleeping")
                    time.sleep(1)
                    t_now = dt.datetime.now()
                    timenow = t_now.strftime("%H:%M")

    comando_voz_usuario()


