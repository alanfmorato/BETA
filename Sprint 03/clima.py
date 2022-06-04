import speech_recognition as sr
import requests
import pyttsx3
# link do open_weather: https://openweathermap.org/
def clima():
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    with sr.Microphone() as source:
        maquina.say("Informe a cidade da qual deseja descobrir a temperatura. ")
        maquina.runAndWait()
        print('ouvindo...')
        voz = audio.listen(source)
        cidade = audio.recognize_google(voz, language='pt-BR')
        maquina.say(cidade)
        API_KEY = "00a7922cfcccb7df823f10e7014e2e42"
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()  # Faz a requisição
        descricao = requisicao_dic['weather'][0]['description']  # Puxa a descrição de como esta o clima
        temperatura = requisicao_dic['main']['temp'] - 273.15  # Puxa a temperatura atual e faz a conversão
        maquina = pyttsx3.init()
        maquina.say(f'Em {cidade} o céu está {descricao} e está {temperatura:.0f}ºC hoje')
        maquina.runAndWait()

