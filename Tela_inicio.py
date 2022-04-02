import requests
from tkinter import *



janela = Tk()
janela.title("Assistente Virtual Agile")

# Definindo o que estará escrito na tela de início e centralizando
texto_inicial = Label(janela, text ="Olá, para iniciar a AGILE clique no botão de start" )
texto_inicial.grid(column=0, row=0)

botao = Button(janela,text="START")
botao.grid(column=0,row=1)

janela.mainloop()
