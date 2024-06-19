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

plt.figure("Gráficos consenoidais", figsize=(10,5))  # 1 linhas, 2 colunas
# plt.subplots_adjust(left= 0.102, right=0.974) # ajuste manual

# Primeiro subplot
ax1 = plt.subplot(1, 2, 1)
plt.plot(x, c)
ax1.set_title("Gráfico do Cosseno")
ax1.set_xlabel("Eixo do Tempo")
ax1.set_ylabel("Eixo da Amplitude")

# Segundo subplot
ax2 = plt.subplot(1, 2, 2)
plt.plot(x, s)
ax2.set_title("Gráfico do Seno")
ax2.set_xlabel("Eixo do Tempo")
ax2.set_ylabel("Eixo da Amplitude")
  # Limitar o eixo y para melhor visualização

# Ajustar o layout: plt.tight_layout() ajusta automaticamente o espaçamento entre os subplots
# para que eles não se sobreponham.
plt.tight_layout()

# Exibir a figura
plt.show()
