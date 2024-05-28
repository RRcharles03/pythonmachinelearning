import random as rdm

#  Criar uma lista e utilizar o metodo choice da lib random

cidades = ['Congonhas', 'Belo Horizonte', 'Uba', 'Nova Iorque', 'Toquio', 'Madrid', 'Seoul']
cidade_escolhida = rdm.choice(cidades)
print(cidade_escolhida)

#  Adicionar novos elementos a minha lista de cidades

cidades_2 = ['Philadelfia', 'São Paulo', 'Londres', 'Roma', 'Cairo']

for e in cidades_2:
  cidades.append(e)

print(cidades)
cidade_escolhida_2 = rdm.choice(cidades)
print(cidade_escolhida_2)