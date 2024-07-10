import matplotlib.pyplot as plt
import matplotlib.style as st
import numpy as np

# O comando abaixo é usado para aplicar um tema especifico ao gráfico
# Para saber os temas disponiveis basta usar o comando st.available
plt.style.use("bmh")

x = np.linspace(0, 2*np.pi, 300, endpoint=True)
y = np.cos(3*x)

fig, axs = plt.subplots(figsize=(10,4))

axs.plot(x, y)
axs.set_title('Gráfico do Cosseno', fontsize=14)
axs.legend(['cos(3x)'])

axs.set_xlabel('Eixo X', fontsize=12)
axs.set_ylabel('Eixo Y', fontsize=12)

# Para customizar as escalas dos eixos, podemos utilizar os metoso xticks e yticks.
# você deve passar um iterável como parametro para os metodos, no exemplo abaixo estou 
# passando um array criado pelo numpy.
plt.xticks(np.arange(0, 2*np.pi+0.5, 0.5)) # acrescentar o valor do intervalo no final.
plt.yticks(np.arange(-1, 1.25, 0.25)) # acrescentar o valor do intervalo no final.


plt.tight_layout()
# Definindo o título da janela da figura
fig.canvas.manager.set_window_title('Aplicando Estilos')
plt.show()
