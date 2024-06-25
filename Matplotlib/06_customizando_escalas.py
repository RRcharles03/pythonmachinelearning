import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 300, endpoint=True)
y = np.cos(3*x)

fig, axs = plt.subplots(figsize=(10,4))

axs.plot(x, y, color='r')
axs.set_title('Gráfico do Cosseno', fontsize=14)
axs.legend(['cos(3x)'])

'''
Básico
O uso mais básico do .legend() é simplesmente chamá-lo após plotar os dados. 
O Matplotlib tentará adivinhar os rótulos a partir das chamadas plot() se você usar o argumento label:
# axs.plot(x, y, label='cos(3x)')
# axs.legend()
'''
'''
Especificando Rótulos Diretos
Se você não forneceu rótulos nas chamadas plot(), 
você pode especificá-los diretamente na chamada para .legend():

loc: Controla a localização da legenda (por exemplo, 'upper right', 'lower left', etc.).
fontsize: Define o tamanho da fonte da legenda.
title: Adiciona um título à legenda.

# axs.legend(loc='upper left', fontsize='small', title='cos(3x)')
# axs.legend(['cos(3x)'])
'''
axs.set_xlabel('Eixo X', fontsize=12)
axs.set_ylabel('Eixo Y', fontsize=12)

# Para customizar as escalas dos eixos, podemos utilizar os metoso xticks e yticks.
# você deve passar um iterável como parametro para os metodos, no exemplo abaixo estou 
# passando um array criado pelo numpy.
plt.xticks(np.arange(0, 2*np.pi+0.5, 0.5)) # acrescentar o valor do intervalo no final.
plt.yticks(np.arange(-1, 1.25, 0.25)) # acrescentar o valor do intervalo no final.

plt.grid(True)
plt.tight_layout()
# Definindo o título da janela da figura
fig.canvas.manager.set_window_title('Customizando Escalas')
plt.show()