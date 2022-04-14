import sounddevice as sd
from scipy.io.wavfile import write
import os

freq = 44100  # Frequência do áudio: 4999 - 64000
seconds = 5  # Duração da gravação

gravacao = sd.rec(int(seconds * freq), samplerate=freq, channels=2)
print("Começando: Fale agora!!")
sd.wait()  # Comando de inicialização da gravação.
print("Fim da gravação!")
write('output.wav', freq, gravacao)  # Salva a gravação como arquivo WAV.
os.startfile("output.wav")           # Abre gravação.


