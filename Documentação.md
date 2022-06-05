<h2 align = "center">
    Documentação
<h4/>

<h1 align = "center"> Assistente Virtual BETA </h1>

<div align="center">
<img src="https://user-images.githubusercontent.com/102003274/160285282-b3d220d2-bf73-4aba-9c86-74a6a4b640b0.png" width="200px" />
</div>

<br>

# TABELA DE CONTEÚDO
<-!---ts----> <br>
    * [Explicação](#Explicação) <br>
    * [Equipe Beta 1](#Equipe-beta-1) <br>
    * [Funcionalidades](#Funcionalidades) <br>
    * [Bibliotecas](#Bibliotecas) <br>



# EXPLICAÇÃO

Essa documentação tem como objetivo direcionar o uso da nossa assistente virtual.

# EQUIPE BETA 1

* Alan Fabrício Morato
* Marcela Ribeiro de Melo
* Ariane Cristine Alves de Sousa
* Elizabeth Cristina Alves Leite
* Larissa Tomé de Souza
* Luiz Henrique Berti
* Tobias Fernandes Bezerra Sousa
* Vitória Brancatti Ramos  Lopes Batista


# FUNCIONALIDADES

Para acessar as funções diga exatamente uma das funções da fala inicial da beta:
**Pesquisa, Pomodoro, Calendário, Toque, Gravador de voz, Livro, Clima, Calculadora ou lembrete**

📌 **Modo pomodoro**
    
Função que auxilia na gestão de tempo em tarefas/estudos. O método possui é dividido em quatro tempos. Primeiro você realiza uma atividade durante 25 minutos, quando acabar o tempo, descansa 5 minutos. Assim sucessivamente até completar três sequências. A quarta rodada possui duração de 25 minutos, porém permite descanso de 30 minutos. O usuário é informado pela assistente virtual o início, hora do intervalo, quantidades de sequências e fim.

📌 **Consulta simples Wikipedia ou Pesquisa**
    
Função que permite ao usuário falar algo que deseja pesquisar na Wikipedia e a assistente virtual retornará o significado. Para utilizar a função é necessário dizer Beta, pesquisa + o que deseja pesquisar.

📌 **Reprodutor de música (toque)**
    
Função que permite ao usuário solicitar que a assistente reproduza alguma música e abrirá na tela Youtube que dará início a música escolhida. Para utilizar a função é necessário dizer Beta, toque + Nome da música.

📌 **Gravador de voz**
    
Função que permite iniciar uma gravação, e posteriormente obter um arquivo no formato wav com o áudio. Para utilizar a função é necessário dizer Beta, gravador de voz.

📌 **Calendário ou Datas**
    
Função que plota na tela uma janela com representação do calendário do mês atual, selecionando em azul o dia vigente. Para utilizar a função é necessário dizer Beta, datas.

📌 **Scraps (livro)**
    
Função que pesquisa na web links de livros que o usuário deseja fazer download. O código retorna um compilado dos 10 primeiros links que aparecem na pesquisa Google e converte o compilado de links em lista em um arquivo pdf. Para utilizar a função é necessário dizer Beta, livro.

📌 **Clima**
    
Função que retorna a temperatura em um município. A assistente virtual pergunta qual a cidade que deseja saber a temperatura e o usuário indica a cidade pelo nome. O código consulta a API: https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br que possui como retorno a temperatura da cidade de entrada e descrição do tempo, Exemplo: se a nuvens, se o dia esta ensolarado, entre outros.) Para utilizar a função é necessário dizer Beta, clima.

📌 **Calculadora**
    
Função que permite realizar operações matemáticas por controle de voz. É necessário inserir como entrada dois números e escolher a operação, entre as opções estão: soma, subtração, multiplicação, divisão e potencialização. Para utilizar a função é necessário dizer Beta, calculadora.

📌 **Lembrete**
    
Função que permite armazenar em um arquivo txt dados de tarefa e data através de reconhecimento de voz, e posteriormente é permitido consultá-los pelo menu da função. Para utilizar a função é necessário dizer Beta, lembrete.


# BIBIOTECAS

- ✅ [SpeechRecognition 3.8.1](https://pypi.org/project/SpeechRecognition/)
- ✅ [Wikipedia](https://pypi.org/project/wikipedia/)
- ✅ [Time](https://pypi.org/project/time/)
- ✅ [Datetime](https://pypi.org/project/DateTime/)
- ✅ [Tkinter](https://pypi.org/project/tk-tools/)
- ✅ [Winsound](https://pypi.org/project/wav-win-sound/)
- ✅ [pyttsx3](https://pypi.org/project/pyttsx3/)
- ✅ [messagebox](https://pypi.org/project/PyMsgBox/)
- ✅ [tkcalendar](https://pypi.org/project/tkcalendar/)
- ✅ [datetime](https://pypi.org/project/DateTime/)
- ✅ [pywhatkit](https://pypi.org/project/pywhatkit/)
- ✅ [sounddevice](https://pypi.org/project/sounddevice/)
- ✅ [scipy.io.wavfile](https://pypi.org/project/scipy/)
- ✅ [write](https://pypi.org/project/write/)
- ✅ [os](https://pypi.org/project/os-sys/)
- ✅ [reportlab.pdfgen](https://pypi.org/project/reportlab/)
- ✅ [canvas](https://pypi.org/project/canvas/)
- ✅ [reportlab.lib.pagesizes](https://pypi.org/project/reportlab/)
- ✅ [requests](https://pypi.org/project/requests/)


