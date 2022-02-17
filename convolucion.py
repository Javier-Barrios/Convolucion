#Javier Andrés Barrios del Aguila
#201801376

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import wave

file = wave.open('Avicii.wav')
audio = file.readframes(-1)
audio = np.frombuffer (audio, dtype=np.int16)

#Grafica Original
#plt.plot(audio)
#plt.title("Wake me up")
#plt.show()

#Grafica Modificada
#Audio Modificado
alfa = np.array([1.,0.,0.,0])
audio_modificado = np.convolve(audio, alfa)

audio_modificado = audio_modificado.astype(np.int16)
write('Avicii_modificado.wav', 40000, audio_modificado)

plt.plot(audio_modificado)
plt.title("Wake me up Modificada")
plt.show()