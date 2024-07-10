from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(1, 5, 500)
y = np.log10(x)

plt.style.use('ggplot')

fig, axs = plt.subplots(figsize=(10,4))
axs.plot(x, y, lw=1.2)

# Plotando a linha horizontal
# No eixo x : o 0 indica o inicio e o 2.5 o fim, ou seja ate onde queremos plotar o marcador.
# No eixo y : seguimos a mesma ideia, no caso sem variaçao. 
# linestyle='--': processar uma linha tracejada
# lw=0.8: line weight, para mudar a espessura da linha.
axs.plot([0, 2.5], [0.4, 0.4], color='g', linestyle='--', lw=0.8)

# Plotar a linha no eixo Y, precisamos olhar primeiro para o eixo x. A ideia é seguir o 
# mesmo pensamento anterior.
axs.plot([2.5, 2.5], [0, 0.4], color='g', linestyle='--', lw=0.8)

# Inserindo o marker 
axs.plot(2.5, 0.4, marker= 'o', color='g')

# Modificar a escala do eixo x
axs.set_xticks(np.arange(0, 5.5, 0.5))
plt.show()