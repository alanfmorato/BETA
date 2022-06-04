import speech_recognition as sr
import pyttsx3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def livros():
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.runAndWait()
    with sr.Microphone() as source:
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        consulta = comando.replace('livro', '')
        maquina.say('Estou pesquisando o livro que pediu')
        maquina.runAndWait()
        consulta = comando.replace('livro', '')
        try:
            from googlesearch import search
        except ImportError:
            maquina.say("Resultado não encontrado")
            maquina.runAndWait()
        X = []
        for j in search(consulta, tld="co.in", num=10, stop=10,
                                    pause=2):
            X.append(j)
            print(X)
            def mm2p(milimetros):
                return milimetros / 0.352777
            cnv = canvas.Canvas('SUA_PESQUISA.pdf', pagesize=A4)
            eixo = 250
            for i in range(0, 10):
                cnv.drawString(mm2p(20), mm2p(eixo), X[i])
                eixo -= 5
                cnv.save()
                maquina.say('Foram pesquisados 10 links que estão salvos em pdf em sua pasta downloads')
                maquina.runAndWait()
