import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0,2* np.pi, 500)
x = np.linspace(0, 10, 100)
c = np.cos(x)
s = np.sin(x)
y = np.tan(x)
z = np.exp(x)

# Utilizando o metodo subplot podemos criar varios gráficos dentro de uma mesma figura.abs

# Criar subplots: plt.subplots(2, 1) cria uma figura com dois subplots (2 linhas e 1 coluna). 
# fig é a figura que contém os subplots, e axs é uma matriz de eixos (subplots).

fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 linhas, 2 colunas

# Primeiro subplot
axs[0,0].plot(x, c, label='Cosseno')
axs[0,0].set_title('Onda Cossenoidal')
axs[0,0].legend()

# Segundo subplot
axs[0,1].plot(x, s, label='Seno', color='r')
axs[0,1].set_title('Onda Senoidal')
axs[0,1].legend()

# Terceiro subplot
axs[1,0].plot(x, y, label='Tangente', color='g')
axs[1,0].set_title('Onda Tangencial')
axs[1,0].legend()
axs[1, 0].set_ylim(-10, 10)  # Limitar o eixo y para melhor visualização

# Quarto subplot
axs[1,1].plot(x, z, label='Exponencial', color='y')
axs[1,1].set_title('Função Exponencial')
axs[1,1].legend()
axs[1, 1].set_ylim(0, 10000)  # Limitar o eixo y para melhor visualização

# Ajustar o layout: plt.tight_layout() ajusta automaticamente o espaçamento entre os subplots
# para que eles não se sobreponham.
plt.tight_layout()

# Exibir a figura
plt.show()
