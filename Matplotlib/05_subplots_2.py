import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y1 = x**2
y2 = x**3
y3 = x**4
y4 = x**5

# Outra forma de fazer subplots

# fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2 ,figsize=(8,4)) #1 linha, 2 colunas
# ax1.plot(x, y1)
# ax2.plot(x, y2)
# plt.show()


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2 , figsize=(16,8)) #2 linhas, 2 colunas
plt.suptitle('Gráficos com Subplots')

ax1.plot(x, y1)
ax1.set_title("Função $x^2$")
ax1.set_xlabel("Tempo")
ax1.set_ylabel("Amplitude")
ax1.grid(True)

ax2.plot(x, y2, color='r')
ax2.set_title("Função $x^3$")
ax2.set_xlabel("Tempo")
ax2.set_ylabel("Amplitude")
ax2.grid(True)

ax3.plot(x, y3, color='y')
ax3.set_title("Função $x^4$")
ax3.set_xlabel("Tempo")
ax3.set_ylabel("Amplitude")
ax3.grid(True)

ax4.plot(x, y4, color='g')
ax4.set_title("Função $x^5$")
ax4.set_xlabel("Tempo")
ax4.set_ylabel("Amplitude")
ax4.grid(True)

plt.tight_layout()
plt.show()