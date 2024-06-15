import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 100)
y_cos = np.cos(2*t)
y_sen = np.sin(2*t)

# O comando abaixo indica que vai ser gerada uma figure pelo matplotlib para posterior inserção do grafico.
# Ex:plt.figure(nome_figure)

plt.figure('Figura do Cosseno')
plt.plot(t, y_cos)
plt.title('Gráfico do Cosseno ')
plt.xlabel('Tempo(seg)')
plt.ylabel('Amplitude')

plt.figure('Figura do Seno')
plt.plot(t, y_sen)
plt.title('Gráfico do Seno ')
plt.xlabel('Tempo(seg)')
plt.ylabel('Amplitude')

plt.show()