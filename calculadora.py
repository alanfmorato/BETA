import speech_recognition as sr
import pyttsx3


while True:
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.say('oi')
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
        if 'calculadora' in comando:
            audio = sr.Recognizer()
            maquina = pyttsx3.init()
            with sr.Microphone() as source:
                maquina.say("Informe o primeiro número: ")
                maquina.runAndWait()
                print('ouvindo...')
                voz = audio.listen(source)
                n1 = audio.recognize_google(voz, language='pt-BR')
                n1 = int(n1)
                print(n1)
            with sr.Microphone() as source:
                maquina.say("Informe o segundo número: ")
                maquina.runAndWait()
                print('Ouvindo...')
                voz = audio.listen(source)
                n2 = audio.recognize_google(voz, language='pt-BR')
                n2 = int(n2)
                print(n2)
            audio = sr.Recognizer()
            maquina = pyttsx3.init()
            maquina.say('Qual operação você deseja efetuar?')
            maquina.runAndWait()
            with sr.Microphone() as source:
                print('Ouvindo...')
                voz = audio.listen(source)
                comando = audio.recognize_google(voz, language='pt-BR')
                comando = comando.lower()
                if 'soma' in comando:
                    mais = n1 + n2
                    maquina.say(f'O resultado é {mais}')


    comando_voz_usuario()



