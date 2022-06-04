from tkinter import *
import principal

janela = Tk()
janela.title('Beta')
janela.iconbitmap(default="beta.ico")
janela.geometry("315x350+500+200")
janela.configure(bg='grey21')
janela.attributes('-alpha', 0.9 , )
microfone=PhotoImage(file="microfone1.png")
microfone = microfone.subsample(5, 5)
p = Button(janela, image=microfone, command=principal.principal, width=60, height=60, compound=TOP, bg='grey21')
p.grid(column=1, row=3, padx=5, pady=15)
beta = PhotoImage(file="beta.png")
beta = beta.subsample(2,2)
proseg = Label(janela, bg="grey21", fg='white', image=beta)
proseg.grid(column=1, row=2, padx=10, pady=10)
acoes = Label(janela, text='Aperte o microfone para começarmos!', bg="MidnightBlue", font=("Verdana", 10))
acoes.grid(column=1, row=5, padx=10, pady=10)
janela.mainloop()

