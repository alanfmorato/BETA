import speech_recognition as sr
import pyttsx3
import pywhatkit

#As bibliotecas acima estão sendo importada para o reconhecimento de determinadas funções que serão utilizadas
#ao decorrer do programa.
#SpeechRecognition é uma bibliotea utilizada para o reconhecimento de voz
#pyttsx3 é uma biblioteca utilizada para a sintetização de voz
#pywhatkit é uma biblioteca utilizada para mandar mensagens para wpp, assistir videos no youtube, etc.

#A função executa_comando serve para reconhecer a voz, habilitar o microfone e entender o que o usuário está falando.
def executa_comando():
    audio = sr.Recognizer() #Reconhecendo a voz e armazenando na variável audio
    maquina = pyttsx3.init() #iniciando a biblioteca pyttsx3
    try: #criando um bloco para entender o que usuário falou
        with sr.Microphone() as source: # abrindo o microfone
            print('Ouvindo')
            voz = audio.listen(source) #Escuta o que o usuário está falando
            comando = audio.recognize_google(voz, language='pt-BR') #Entende de acordo com a linguagem o que o usuário está falando
            if 'helpi' in comando:
                comando = comando.replace('helpi', '')#retirando o nome helpi do comando
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está funcionando')# Se o microfone não estiver funcionando, ele retornará essa mensagem

    return executa_comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'toque' in comando:
        musica = comando.replace('toque','')#retirando o nome helpi do comando
        resultado = pywhatkit.playonyt(musica)#função para abrir a musica no youtube
        maquina.say('tocando musica')
        maquina.runAndWait()#stand by

comando_voz_usuario()