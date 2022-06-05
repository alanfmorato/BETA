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
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import requests

while True:
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.say('Olá, meu nome é BÉTA, Qual função deseja acessar? Pesquisa, Pomodoro, Calendário, Toque, Gravador de voz, Livro, Clima, Calculadora ou lembrete')
    maquina.runAndWait()
    pesquisa = pyttsx3.init()
    pesquisa.say
    pesquisa.runAndWait()
    pomodoro = pyttsx3.init()
    pomodoro.say
    pomodoro.runAndWait()
    toque = pyttsx3.init()
    toque.say
    toque.runAndWait()
    gravador = pyttsx3.init()
    gravador.say
    gravador.runAndWait()
    livro = pyttsx3.init()
    livro.say
    livro.runAndWait()
    clima = pyttsx3.init()
    clima.say
    clima.runAndWait()
    calculadora = pyttsx3.init()
    calculadora.say
    calculadora.runAndWait()
    lembretes = pyttsx3.init()
    lembretes.say
    lembretes.runAndWait()



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
            pesquisa.say(resultado)
            pesquisa.runAndWait()
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
        elif 'toque' in comando:
            musica = comando.replace('toque', '')
            resultado = pywhatkit.playonyt(musica)
            toque.say('Iniciando musica')
            toque.runAndWait()
        elif 'gravador de voz' in comando:
            freq = 44100
            seconds = 10

            gravacao = sd.rec(int(seconds * freq), samplerate=freq, channels=2)
            print("Começando: Fale agora!!")
            sd.wait()
            print("Fim da gravação!")
            write('output.wav', freq, gravacao)
            os.startfile("output.wav")
        elif 'livro' in comando:
            livro.say('Estou pesquisando o livro que pediu')
            livro.runAndWait()
            consulta = comando.replace('livro', '')
            try:
                from googlesearch import search
            except ImportError:
                print("Resultado não encontrado")
            X = []
            for j in search(consulta, tld="co.in", num=10, stop=10,
                            pause=2):  # Retorna um compilado dos 10 primeiros links que aparecem na pesquisa google
                X.append(j)  # Converte o compilado de links em lista para manipular sua posição no pdf
            print(X)

            def mm2p(milimetros):
                return milimetros / 0.352777  # converte pontos em milimetros

            cnv = canvas.Canvas('SUA_PESQUISA.pdf', pagesize=A4)  # Define o nome do arquivo pdf e o tamanho da página

            eixo = 250

            for i in range(0, 10):
                cnv.drawString(mm2p(20), mm2p(eixo), X[i])
                eixo -= 5  # colocado menos para os links aparecerem na ordem correta
            cnv.save()  # salva o pdf na pasta downloads do PC

            livro.say('Foram pesquisados 10 links que estão salvos em pdf em sua pasta downloads')
            livro.runAndWait()
        elif 'clima' in comando:
            audio = sr.Recognizer()
            maquina = pyttsx3.init()
            with sr.Microphone() as source:
                clima.say("Informe a cidade da qual deseja descobrir a temperatura. ")
                clima.runAndWait()
                print('ouvindo...')
                voz = audio.listen(source)
                cidade = audio.recognize_google(voz, language='pt-BR')
                print(cidade)


                API_KEY = "00a7922cfcccb7df823f10e7014e2e42"
                link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

                requisicao = requests.get(link)
                requisicao_dic = requisicao.json()  # Faz a requisição
                descricao = requisicao_dic['weather'][0]['description']  # Puxa a descrição de como esta o clima
                temperatura = requisicao_dic['main']['temp'] - 273.15  # Puxa a temperatura atual e faz a conversão
                maquina = pyttsx3.init()
                clima.say(f'Em {cidade} o céu está {descricao} e está {temperatura:.0f}ºC hoje')
                clima.runAndWait()

        elif 'calculadora' in comando:
            audio = sr.Recognizer()
            maquina = pyttsx3.init()
            with sr.Microphone() as source:
                calculadora.say("Informe o primeiro número: ")
                calculadora.runAndWait()
                print('ouvindo...')
                voz = audio.listen(source)
                n1 = audio.recognize_google(voz, language='pt-BR')
                n1 = int(n1)
                print(n1)
            with sr.Microphone() as source:
                calculadora.say("Informe o segundo número: ")
                calculadora.runAndWait()
                print('Ouvindo...')
                voz = audio.listen(source)
                n2 = audio.recognize_google(voz, language='pt-BR')
                n2 = int(n2)
                print(n2)
            audio = sr.Recognizer()
            maquina = pyttsx3.init()
            calculadora.say('Qual operação você deseja efetuar?')
            calculadora.runAndWait()
            with sr.Microphone() as source:
                print('Ouvindo...')
                voz = audio.listen(source)
                comando = audio.recognize_google(voz, language='pt-BR')
                comando = comando.lower()
                if 'soma' in comando:
                    mais = n1 + n2
                    calculadora.say(f'O resultado é {mais}')
                elif 'divisão' in comando:
                    barra = n1 / n2
                    calculadora.say(f'O resultado é {barra:.2f}')
                elif 'subtração' in comando:
                    sub = n1 - n2
                    calculadora.say(f'O resultado é {sub:.2f}')
                elif 'multiplicação' in comando:
                    mut = n1 * n2
                    calculadora.say(f'O resultado é {mut:.2f}')
                elif 'potencialização' in comando:
                    pot = n1 ** n2
                    calculadora.say(f'O resultado é {pot:.2f}')

        if 'lembrete' in comando:
            audio = sr.Recognizer()
            maquina = pyttsx3.init()
            with sr.Microphone() as source:
                lembretes.say(
                    "VOCÊ DESEJA CADASTRAR?"
                )
                lembretes.runAndWait()
                print('Ouvindo...')
                voz = audio.listen(source)
                comando = audio.recognize_google(voz, language='pt-BR')
                comando = comando.lower()
                if 'cadastrar' in comando:
                    with sr.Microphone() as source:
                        lembretes.say("Diga o que deseja lembrar: ")
                        lembretes.runAndWait()
                        print('Ouvindo...')
                        voz = audio.listen(source)
                        tarefa = audio.recognize_google(voz, language='pt-BR')
                        tarefa = str(tarefa)
                        print(tarefa)
                    with sr.Microphone() as source:
                        lembretes.say("Qual data você deseja lembrar:")
                        lembretes.runAndWait()
                        print('Ouvindo...')
                        voz = audio.listen(source)
                        data = audio.recognize_google(voz, language='pt-BR')
                        data = str(data)
                        print(data)
                    lembrete = open("lembrete.txt", "a")
                    dados = f'{tarefa};{data}\n'
                    lembrete.write(dados)
                    lembrete.close()
                    lembretes.say(f'Lembrete gravado com sucesso!')
                    abrir = open(r"C:\Users\morat\Downloads\lembrete.txt", 'r')
                    for i in abrir:
                        print(i)
                    maquina.runAndWait()

    comando_voz_usuario()
